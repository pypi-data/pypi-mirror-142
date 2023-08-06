import os
import zipfile

"""
Process zip source
"""


def process(hub, name: str, source: str, sourcePath: str):
    if source in hub.idem.RUNS[name]["processed_sls_sources"]:
        return
    if zipfile.is_zipfile(sourcePath):
        zipSource = zipfile.ZipFile(sourcePath)
        processed_sls_cache_dir = os.path.join(
            hub.idem.RUNS[name]["cache_dir"], "processed_sls"
        )
        c_dir = os.path.join(processed_sls_cache_dir, sourcePath.lstrip(os.sep))
        os.makedirs(c_dir, exist_ok=True)
        zipSource.extractall(c_dir)
        hub.idem.RUNS[name]["processed_sls_sources"][source] = c_dir
