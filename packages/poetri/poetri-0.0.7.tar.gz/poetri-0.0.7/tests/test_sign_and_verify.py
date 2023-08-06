#!/usr/bin/env python
import unittest
import json
import os
from poetri.sign_jwk import sign_jwk
from poetri.verify_jws_with_jwk import verify_jws_with_jwk
from collections import OrderedDict
from jwcrypto import jwt, jwk

__author__ = 'Alan Viars @aviars'


class TestSignAndVerify(unittest.TestCase):

    def setUp(self):

        # Get the kid/issuer
        self.issuer = "example.com"
        self.expires = 630720000
        # load a sample payload
        payload_fp = os.path.join(os.path.dirname(__file__), "payload.json")
        payload_fh = open(payload_fp)
        payload = payload_fh.read()
        self.payload = json.loads(payload, object_pairs_hook=OrderedDict)
        payload_fh.close()

        # load a sample keypair
        keypair_fp = os.path.join(os.path.dirname(__file__), "private.jwk")
        keypair_fh = open(keypair_fp)
        keypair = keypair_fh.read()
        self.privkey = json.loads(keypair, object_pairs_hook=OrderedDict)
        keypair_fh.close()

        # load a sample public key
        pubkey_fp = os.path.join(os.path.dirname(__file__), "public.jwk")
        pubkey_fh = open(pubkey_fp)
        pubkey = pubkey_fh.read()
        self.pubkey = json.loads(pubkey, object_pairs_hook=OrderedDict)
        pubkey_fh.close()

        # A public key that doesn't match its private counterpart.
        self.bad_n = "X0vZedyiaeg_tqAcGeVzdpd_DO5QtBHpsRvDX6SKDwOytfsLZUIfR5Q"\
                     "gpz49kLCEDIjGAdg3iQ81leo2zrX5RfZ6q1n5pFpbU7VLX3ylKZ7Sug"\
                     "-ujuiNd7xmVnvdwiKyupnEnG_6XXwJDaoyMT9xXgiR4BKS3pHCoIPO0"\
                     "ktIi2BHGB1Nqb2YqKoCaeMmuZvW6EIA04_wb6wTLIXcf8jh8bt4pJ0C"\
                     "WMLqJqr524p0rEhYGl5P3BsnBDr19vM-i-_dNjAoaUT1Bc6wN_a1wFe"\
                     "baEL1C2Aia1EeF3oMAfsa_aTLA2x8NlWrjwwPyGIOsrxjmjJ6oLqvUC"\
                     "dcg1Nod9YaY9"

    def test_signing(self):

        self.signed_jws = sign_jwk(self.payload,
                                   self.privkey,
                                   self.expires)
        """Test the POET JWT signing by ensuring
           exactly two periods in output."""
        self.assertEqual(self.signed_jws.count('.'), 2)

    def test_signature_verification_good_pubkey(self):
        self.signed_jws = sign_jwk(self.payload,
                                   self.privkey,
                                   self.expires)
        self.cerification_result = verify_jws_with_jwk(
            self.signed_jws, self.pubkey)
        self.assertTrue(self.cerification_result)

    def test_signature_verification_expires_is_working(self):
        """Set it to expire now"""
        self.signed_jws = sign_jwk(self.payload, self.privkey, 0)
        key = jwk.JWK(**self.privkey)
        myjwt = jwt.JWT(key=key, jwt=self.signed_jws)
        claims = json.loads(myjwt.claims)
        self.assertAlmostEqual(claims['iat'], claims['exp'])

    def test_signature_verification_good_pubkey_bad_kid(self):
        self.signed_jws = sign_jwk(self.payload, self.privkey)
        self.pubkey['kid'] = self.pubkey['kid'] + "foo"
        self.verified_payload = verify_jws_with_jwk(
            self.signed_jws, self.pubkey)


if __name__ == '__main__':
    unittest.main()
