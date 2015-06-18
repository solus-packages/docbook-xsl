#!/usr/bin/env python
import os
import os.path

def postInstall(fromVersion, fromRelease, toVersion, toRelease):
    os.system ("/usr/bin/build-docbook-catalog --version=4.5")
