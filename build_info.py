#!/usr/bin/python
import os
import re

SETTINGS_GRADLE = 'settings.gradle'
BUILD_GRADLE = 'build.gradle'

REGEX_MODULE = '\s*include\s*[\']:(\S+)[\']'
REGEX_DEP_1 = '\s*([^\s(]+)\s*\(?[\'\"]([^\s(]+):([^\s(]+):([^\s(]+)[\'\"]'
REGEX_DEP_2 = '\s*([^\s(]+)\s*\(? group:\s*[\'\"](\S+)[\'\"]\s*,\s*name:\s*[\'\"](\S+)[\'\"]\s*,\s*version:\s*[\'\"](\S+)[\'\"]\s*'

REGEX_EXTRA_PROPS = '[^ext\.?]?(\s*\S+\s*)=\s*([^\n]*)'

REGEX_PROPS = '\s+(compileSdkVersion|buildToolsVersion)\s+\$?\'?\"?([\w\.\-]+)\'?\"?'

extra_props = {}


class BuildInfo:
    @staticmethod
    def fetch():

        build_info = {}

        # root gradle info
        build_info.update(process_root_module())

        # module dependencies & other info e.g. compileSdkVersion, buildToolsVersion..
        process_modules(build_info)

        return {"build": build_info}


def process_root_module():
    global extra_props
    deps = {'deps': []}
    with open('build.gradle', 'r') as f:
        reg = re.compile(REGEX_EXTRA_PROPS, re.MULTILINE)
        reg_dep = re.compile(REGEX_DEP_1, re.MULTILINE)
        for line in f:

            # process extra properties
            match = reg.match(line)
            if match:
                data = re.split('=', match.group().replace('ext.', '').replace(' ', ''))  # todo
                extra_props[data[0]] = data[1]

            # process root dependencies
            match = reg_dep.match(line)
            if match:
                deps['deps'] += [{'config': match.group(1),
                                  'group': match.group(2),
                                  'name': match.group(3),
                                  'version': match.group(4)}]
    return deps


def process_modules(json):
    with open(SETTINGS_GRADLE) as f:
        modules_found = []
        for line in f:
            match = re.compile(REGEX_MODULE, re.VERBOSE).match(line)
            if match:
                line = line.replace('include', '')
                modules = re.findall(r'[:\w+]+', line)
                modules_found.extend(modules)

        for module in modules_found:
            process_module(module, json)

        return json


def process_module(module, json):
    module = module.replace(':', '')
    with open(module + os.path.join(module, '/build.gradle')) as f:
        process_module_dependencies(f, module, json)


def process_module_dependencies(f, module, json):
    global extra_props
    regex1 = re.compile(REGEX_DEP_1, re.VERBOSE)
    regex2 = re.compile(REGEX_DEP_2, re.VERBOSE)

    for line in f:

        match = regex1.match(line) or regex2.match(line)
        if match:
            version = match.group(4)
            if version.startswith(("$", "rootProject")):
                version = extra_props[version.split('.')[-1]].replace("\"", "")
            json['deps'] += [{'config': match.group(1),
                              'group': match.group(2),
                              'name': match.group(3),
                              'version': version,
                              'module': module}]

        match = re.compile(REGEX_PROPS, re.VERBOSE).match(line)
        if match:
            value = match.group(2)
            if value.startswith(("$", "rootProject")):
                value = extra_props[value.split('.')[-1]]
            json.update({match.group(1): value.replace('\"', '')})
