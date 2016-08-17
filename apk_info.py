#!/usr/bin/python
import os
import shlex
import subprocess
import re


class ApkInfo:
    @staticmethod
    def fetch(main_module, build_variant):

        # apk_folder_path = os.path.join(main_module, 'build', 'outputs', 'apk')
        apk_folder_path = os.path.join('sample', main_module, 'build', 'outputs', 'apk')

        # we're expecting only one apk
        apk_file = [i for i in os.listdir(apk_folder_path) if  re.match(r'.*' + build_variant + '.apk', i)]
        if len(apk_file) is 0:
            raise Exception('Can\'t find apk related to given build variant [' + build_variant + ']')

        apk_path = os.path.join(apk_folder_path, apk_file[0])

        # method count
        classes_dex_path = os.path.join('sample', main_module, 'build', 'intermediates', 'dex',
                                        *build_variant.split('-'))
        classes_dex_path = classes_dex_path + '/classes.dex'
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

        # Last item is None, remove it
        del permissions[len(permissions) - 1]

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
