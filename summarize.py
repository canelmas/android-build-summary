#!/usr/bin/python
import json
import sys

from apk_info import ApkInfo
from build_info import BuildInfo
from jenkins_info import JenkinsInfo


def summarize():
    if len(sys.argv) > 2:
        for build_variant in sys.argv[2:]:

            summary = {}

            # Build Info
            summary.update(BuildInfo.fetch())

            # Apk Info
            summary.update(ApkInfo.fetch(sys.argv[1], build_variant))

            # Jenkins info
            summary.update(JenkinsInfo.fetch())

            print json.dumps(summary, indent=4)
    else:
        help()

def help():
    print "usage : ./summarize.py <main_module_name> <build_variant_1>...<build_variant_n>\n"
    print "Ex: ./summarize.py app prod-release lite-release local-debug\n"


if __name__ == '__main__':
    summarize()
