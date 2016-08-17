#!/usr/bin/python

import os


class JenkinsInfo:
    @staticmethod
    def fetch():
        return {'jenkins': {"id": os.getenv('BUILD_ID', None),
                            "node": os.getenv('NODE_NAME', None),
                            "commit": os.getenv('GIT_COMMIT', None),
                            "branch": os.getenv('GIT_BRANCH', None),
                            "url": os.getenv('GIT_URL', None)}}
