#!/usr/bin/env python
from jwcrypto import jwk
import json
import sys
from collections import OrderedDict

# Copyright 2022 Videntity Systems, Inc.
__author__ = 'Alan Viars @aviars'


def gen_jwk_public(private_key_jwk):

    key = jwk.JWK(**private_key_jwk)
    publickey = json.loads(key.export(private_key=False))
    return(publickey)


# Command line app.
if __name__ == "__main__":

    if len(sys.argv) != 2:
        print("Usage:")
        print("generate_jwk_public.py [JWK_PRIVATE_FILE_PATH]")
        print("generate_jwk_public.py my-private-key.jwk")
        sys.exit(1)
    my_jwk_file = sys.argv[1]
    my_jwk_fh = open(my_jwk_file)

    try:
        k = my_jwk_fh.read()
        my_jwk = json.loads(k, object_pairs_hook=OrderedDict)
    except ValueError:
        print("Error parsing the JWK.", str(sys.exc_info()))
        exit(1)

    result = gen_jwk_public(my_jwk)
    my_jwk_fh.close()
    print(json.dumps(result, indent=4))
