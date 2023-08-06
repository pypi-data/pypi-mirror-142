#!/usr/bin/env python
import sys
import json
import time
from collections import OrderedDict
from jwcrypto import jwk, jwt
from jwcrypto.jws import InvalidJWSSignature

# Copyright 2022 - Videntity Systems, Inc.
__author__ = 'Alan Viars @aviars'


def verify_jws_with_jwk(my_jws, my_jwk_dict):

    # load the Signed JWT (aka JWS)
    my_jws = my_jws.strip()
    k = my_jwk_dict
    key = jwk.JWK(**k)
    e = my_jws

    try:
        ET = jwt.JWT(key=key, jwt=e)
        # print("ET",ET.claims)
        claims = json.loads(ET.claims)
        # Make sure its not expired
        if 'iat' in claims.keys():
            if claims['exp'] <= int(time.time()):
                return False
        if 'iss' in claims.keys():
            if claims['iss'] == my_jwk_dict['kid']:
                return True
        return False
    except InvalidJWSSignature:
        return False


# command line application
if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage:")
        print("verify_jws_with_jwk.py [JWS_FILE_PATH] [JWK_PUBLIC_FILE_PATH]")
        print("Example: verify_jws_with_jwk.py myapp.jwt public.jwk")
        sys.exit(1)

    my_jwt_file = sys.argv[1]
    my_jwk_file = sys.argv[2]
    jwt_fh = open(my_jwt_file)
    jwk_fh = open(my_jwk_file)

    # Ensure JWK is a JSON object
    try:
        k = jwk_fh.read()
        my_jwk_dict = json.loads(k, object_pairs_hook=OrderedDict)
    except ValueError:
        print("Error parsing the JWK.", str(sys.exc_info()))
        exit(1)

    result = verify_jws_with_jwk(jwt_fh.read(), my_jwk_dict)
    result = json.dumps({"jwk_signature_veification_result": result}, indent=4)
    jwt_fh.close()
    jwk_fh.close()
    print(result)
