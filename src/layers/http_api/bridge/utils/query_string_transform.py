"""..."""
from __future__ import annotations


def _get_query_string(**kwargs):
    params = [f"{x[0]}={x[1]}" for x in kwargs.items()]
    return "&".join(params)
