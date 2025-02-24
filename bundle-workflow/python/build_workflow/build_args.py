# Copyright OpenSearch Contributors.
# SPDX-License-Identifier: Apache-2.0

import sys
import argparse

class BuildArgs():
    manifest: str
    snapshot: bool
    component: str
    
    def __init__(self):
        parser = argparse.ArgumentParser(description = "Build an OpenSearch Bundle")
        parser.add_argument('manifest', type = argparse.FileType('r'), help="Manifest file.")
        parser.add_argument('-s', '--snapshot', action = 'store_true', default = False, help="Build snapshot.")
        parser.add_argument('-c', '--component', type = str, help="Rebuild a single component.")
        args = parser.parse_args()
        self.manifest = args.manifest
        self.snapshot = args.snapshot
        self.component = args.component

    def script_path(self):
        return sys.argv[0].replace('/python/build.py', '/build.sh')

    def component_command(self, name):
        return ' '.join(filter(None, [
            self.script_path(),
            self.manifest.name,
            f'--component {name}',
            f'--snapshot' if self.snapshot else None
        ]))
