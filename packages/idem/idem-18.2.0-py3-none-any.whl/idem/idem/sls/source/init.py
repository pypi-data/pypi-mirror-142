"""
This file contains routines to handles/prepare sls-sources to be processed by rend.
"""
import mimetypes
import os


def process(hub, name: str):

    for source in hub.idem.RUNS[name]["sls_sources"]:
        if source.startswith("file://"):
            sourcePath = source[7:]
            if os.path.isfile(sourcePath):
                filemimetypes = mimetypes.guess_type(sourcePath)
                if filemimetypes and filemimetypes[0] == "application/zip":
                    hub.idem.sls.source.zip_source.process(name, source, sourcePath)
