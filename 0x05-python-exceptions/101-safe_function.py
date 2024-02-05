#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as E:
        sys.stderr.write("Exception: {}\n".format(E))
        res = None
    finally:
        return res
