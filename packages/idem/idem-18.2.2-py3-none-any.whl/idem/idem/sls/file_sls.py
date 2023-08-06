"""
This module is used to retrive files from a local source
"""
import os
from typing import Dict


__virtualname__ = "file"


async def cache(hub, source: str, loc: str) -> Dict or None:
    """
    Take a file from a location definition and cache it in memory
    """
    full = os.path.join(source, loc)
    if full.startswith("file://"):
        full = full[7:]
    if not os.path.isfile(full):
        return None
    in_memory_file = None
    with open(full, "rb") as rfh:
        in_memory_file = rfh.read()
    if not in_memory_file:
        return None
    return {full: in_memory_file}
