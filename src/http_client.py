"""
Zero-dependency HTTP helpers built on urllib (Python stdlib only).

The bounty explicitly prefers solutions with no external Python
dependencies beyond stdlib, so every network call in this project
goes through the two functions below instead of `requests`.
"""
import json
import urllib.request
import urllib.error

from . import config


class FetchError(Exception):
    """Raised when an HTTP call fails or returns non-JSON where JSON was expected."""


def get_json(url: str, timeout: int = config.HTTP_TIMEOUT_SECONDS) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": config.HTTP_USER_AGENT, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = resp.read()
            return json.loads(body)
    except urllib.error.HTTPError as e:
        raise FetchError(f"HTTP {e.code} fetching {url}: {e.reason}") from e
    except urllib.error.URLError as e:
        raise FetchError(f"Network error fetching {url}: {e.reason}") from e
    except json.JSONDecodeError as e:
        raise FetchError(f"Non-JSON response from {url}: {e}") from e


def post_json_rpc(url: str, method: str, params: list, timeout: int = config.RPC_TIMEOUT_SECONDS) -> dict:
    """Make a Solana JSON-RPC 2.0 call and return the `result` field."""
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params,
    }).encode("utf-8")

    req = urllib.request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "User-Agent": config.HTTP_USER_AGENT,
        },
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            body = json.loads(resp.read())
    except urllib.error.HTTPError as e:
        raise FetchError(f"HTTP {e.code} calling RPC method {method}: {e.reason}") from e
    except urllib.error.URLError as e:
        raise FetchError(f"Network error calling RPC method {method}: {e.reason}") from e
    except json.JSONDecodeError as e:
        raise FetchError(f"Non-JSON RPC response for {method}: {e}") from e

    if "error" in body:
        raise FetchError(f"RPC error calling {method}: {body['error']}")
    return body.get("result")
