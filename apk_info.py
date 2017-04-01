#!/usr/bin/python
import os
import shlex
import subprocess
import re
import logging


class ApkInfo:
    @staticmethod
    def fetch(main_module, build_variant):
        try:
            # look for the apk file path
            apk_path = look_for_apk_file(main_module, build_variant)

            if len(apk_path) is 0:
                raise Exception('Can\'t find apk related to the given build variant {}'.format(build_variant))

            # method count
            classes_dex_folder = os.path.join(main_module, 'build', 'intermediates', 'dex', *build_variant.split('-'))
            classes_dex_path = classes_dex_folder + '/classes.dex'

            if not os.path.exists(classes_dex_path):
                # >= 1.5.0
                classes_dex_folder = os.path.join(main_module, 'build', 'intermediates', 'transforms', 'dex', *build_variant.split('-'))
                classes_dex_path = classes_dex_folder + '/folders/1000/1f/main/classes.dex'

            method_count = subprocess.Popen(
                'cat ' + classes_dex_path + ' | head -c 92 | tail -c 4 | hexdump -e \'1/4 "%d\n"\'',
                shell=True,
                stdout=subprocess.PIPE
            ).stdout.read()

            method_count = long(method_count)

            # Apk size
            apk_size = to_mb(os.path.getsize(apk_path))

            # Permissions
            cmd_perms = "aapt d permissions {}".format(apk_path)
            permissions = subprocess.check_output(shlex.split(cmd_perms)).split("\n")

            # App id
            app_id = permissions[0].split(':')[1][1:]
            del permissions[0]

            # Beautify permissions
            regex = re.compile("name=\'(\S+)\'")
            permissions = [m.group(1) for l in permissions for m in [regex.search(l)] if m]

            # Min sdk
            min_sdk = sdk_version(apk_path, 'minSdkVersion')

            # Target sdk
            target_sdk = sdk_version(apk_path, 'targetSdkVersion')

            # Version Name
            version_name = version_info_name(apk_path)

            # Version Code
            version_code = version_info_code(apk_path)

            return {"apk": {'apkSize': apk_size,
                            'appId': app_id,
                            'methodCount': method_count,
                            'minSdk': min_sdk,
                            'permissions': permissions,
                            'targetSdk': target_sdk,
                            'versionCode': version_code,
                            'versionName': version_name,
                            'buildVariant': build_variant}}
        except:
            logging.error('Constructing Apk info failed for module={} and build_variant={}'.format(main_module, build_variant))
            raise


def sdk_version(apk_path, name):
    version = read_property(apk_path, name)
    return int(version.split('=')[1].split(')')[1], 16)


def version_info_name(apk_path):
    version_name = read_property(apk_path, 'versionName')
    return version_name[version_name.index('Raw') + 6:-3]


def version_info_code(apk_path):
    version_code = read_property(apk_path, 'versionCode')
    return int(version_code.split('=')[1].split(')')[1], 16)


def read_property(apk_path, name):
    return subprocess.Popen(
        'aapt list -a ' + apk_path + ' | grep ' + name,
        shell=True,
        stdout=subprocess.PIPE
    ).stdout.read()


def to_mb(byte, bsize=1024):
    return "{:.5}".format(float(byte / (bsize * bsize)))


def look_for_apk_file(main_module, build_variant):
    """
    Look for the apk file in the following locations :
        <main_module>/build/outputs/apk (expected default apk location)
        current_working_directory/output-<build_variant> (monitise-mea location)
    """
    apk_path_alternatives = [os.path.join(main_module, 'build', 'outputs', 'apk'),
                             os.path.join(os.getcwd(), 'output-' + build_variant)]

    for alt in apk_path_alternatives:
        apk_file = [i for i in os.listdir(alt) if re.match(r'.*' + build_variant + '.apk', i)]
        if not len(apk_file) is 0:
            return os.path.join(alt, apk_file[0])

    return ""
