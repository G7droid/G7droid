import json
import random
import traceback
from json.decoder import JSONDecodeError
from typing import Optional, Tuple

import httpx

from utils import hc


class GateOffError(Exception):
    pass

async def duckpriv(card: str) -> Tuple[Optional[bool], str]:
    gate = "duckpriv"
    print(f"[GATE_{gate}][{card}] Ta comendo quieto eh?")
    token = "duckpriv"
    try:
        rt = await hc.get(
            f"https://chkdoduck.000webhostapp.com/false.php?lista=",
            params=dict(lista=card),
        )
        rj = rt.text
    except:
        return None, gate

    print(f"[GATE_{gate}][{card}] {rj}")

    rcode = True if 'Aprovada' in rj else False if 'die' in rj else None

    return (rcode, gate)