#!/usr/bin/env python
from jwcrypto import jwk
import json
import sys
import uuid
from collections import OrderedDict

__author__ = 'Alan Viars @aviars'


def gen_jwk_private(kid=None, use='sig'):
    key = jwk.JWK.generate(kty='EC', crv='secp256k1', use=use)
    if not kid:
        key.kid = key.thumbprint()
    else:
        key.kid = kid
    # Includes  "d" so its a private key.
    keypair = json.loads(key.export(), object_pairs_hook=OrderedDict)
    return keypair


# Command line utility application.
if __name__ == "__main__":

    if len(sys.argv) not in (1, 2):
        print("Missing parameters.")
        print("Usage:")
        print("generate_jwk_private.py (KID)")
        print("Note if kid is omitted then the key's thumprint is used instead.")
        sys.exit(1)

    if len(sys.argv) == 2:
        kid = sys.argv[1]
    else:
        kid = None
    result = gen_jwk_private(kid=kid)
    print(json.dumps(result, indent=4))
