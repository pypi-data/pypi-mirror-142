#!/usr/bin/env python
from jwcrypto import jwk, jwt
import json
import sys
import time
from collections import OrderedDict

__author__ = 'Alan Viars @aviars'
# Copyright 2022 Videntity Systems, Inc.


def sign_jwk(payload, private_key_jwk, expires=630720000):

    key = jwk.JWK(**private_key_jwk)

    # Set the headers
    headers = OrderedDict()
    headers["typ"] = "JWT"
    headers["alg"] = "ES256K"

    # Add/overwrite payload
    payload["iss"] = key.key_id
    payload["iat"] = int(time.time())

    # Set the date to expire using seconds from now.
    payload["exp"] = payload["iat"] + expires

    # sign the token
    payload = json.dumps(payload)
    Token = jwt.JWT(header=headers, claims=payload)
    Token.make_signed_token(key)
    return(Token.serialize())


# Command line app.
if __name__ == "__main__":

    if len(sys.argv) not in (3, 4):
        print("Usage:")
        print(
            "sign_jwk.py [PAYLOAD_JSON_FILE] [JWK_PRIVATE_FILE_PATH] [SECONDS_UNTIL_EXPIRY]")
        print("Example: sign_jwk.py mypayload.json private.jwk 31536000")
        print("Note: 31536000 is one year from now.")
        sys.exit(1)

    my_payload_file = sys.argv[1]
    my_jwk_file = sys.argv[2]
    if sys.argv == 4:
        expires = sys.argv[3]
    else:
        expires = 63072000
    my_payload_fh = open(my_payload_file)
    my_jwk_fh = open(my_jwk_file)

    # convert json to dict
    try:
        p = my_payload_fh.read()
        my_payload = json.loads(p, object_pairs_hook=OrderedDict)
    except ValueError:
        result = ["Error parsing the JSON Payload", str(sys.exc_info())]
    try:
        k = my_jwk_fh.read()
        my_jwk = json.loads(k, object_pairs_hook=OrderedDict)
    except ValueError:
        result = ["Error parsing the JWK.", str(sys.exc_info())]
        print(result)

    result = sign_jwk(my_payload, my_jwk, expires)

    my_payload_fh.close()
    my_jwk_fh.close()

    print(result)
