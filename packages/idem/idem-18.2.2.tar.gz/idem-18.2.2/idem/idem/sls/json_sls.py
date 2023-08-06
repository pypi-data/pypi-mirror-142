"""
This module is used to retrieve files from a json source
"""
import json
from typing import Dict

__virtualname__ = "json"


async def cache(hub, source: str, loc: str) -> Dict or None:
    """
    Take a file from a location definition and cache it in memory
    """
    if source.startswith("json://"):
        source = source[7:]

    data = json.loads(source)

    for uuid, values in data.items():
        c_tgt = f"{uuid}.sls"
        # There will only be one item in this dictionary
        return {c_tgt: json.dumps(values).encode("utf-8")}
