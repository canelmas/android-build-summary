#!/usr/bin/python
import json
import requests
import sys
import logging

from datetime import datetime
from apk_info import ApkInfo
from build_info import BuildInfo
from jenkins_info import JenkinsInfo


def summarize():
    if len(sys.argv) > 3:
        for build_variant in sys.argv[3:]:
            try:
                # todo : yoksa ilgili build variant skip

                summary = {}

                # Build Info
                summary.update(BuildInfo.fetch())

                # Apk Info
                summary.update(ApkInfo.fetch(sys.argv[2], build_variant))

                # Jenkins info
                summary.update(JenkinsInfo.fetch())

                # Date & Project Name
                summary.update({'created': str(datetime.now()),
                                'name': sys.argv[1]})

                # print summary
                print json.dumps(summary, indent=4)

                # send it
                requests.put('http://stuff.me/v1/projects',
                             data=json.dumps(summary),
                             headers={'Content-Type': 'application/json;charset=UTF-8'})

            except Exception as error:
                logging.exception(error)
    else:
        help()


def help():
    print "usage : ./summarize.py <project_name> <main_module_name> <build_variant_1>...<build_variant_n>\n"
    print "Ex: ./summarize.py lovely-app-android app prod-release lite-release local-debug\n"


if __name__ == '__main__':
    summarize()
