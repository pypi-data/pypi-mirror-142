#!/usr/bin/env python
import unittest
import json
from poetri.generate_jwk_private import gen_jwk_private
from poetri.generate_jwk_public import gen_jwk_public

# Copyright Videntity Systems, Inc.
__author__ = 'Alan Viars @aviars'


class TestJWKGeneration(unittest.TestCase):
    mykey = "example.com"
    private_key = gen_jwk_private(mykey)
    expected_private_jwk_keys = ['kty', 'd', 'use', 'kid', 'crv', 'x', 'y']
    expected_public_keys = ['kty', 'use', 'kid', 'crv', 'x', 'y']

    def setUp(self):
        pass

    def test_generate_jwk_keypair(self):
        """Assert expected keys are in output"""
        pk = self.private_key
        for k in pk:
            self.assertIn(k, self.expected_private_jwk_keys)

        self.assertEqual(pk['kty'], 'EC')
        self.assertEqual(pk['use'], 'sig')
        self.assertEqual(pk['crv'], 'secp256k1')
        self.assertEqual(pk['kid'], self.mykey)

    def test_gen_public(self):
        public_key = gen_jwk_public(self.private_key)

        """Assert expected keys are in output"""
        for k in self.expected_public_keys:
            self.assertIn(k, public_key.keys())
        self.assertNotIn('d', public_key.keys())

        self.assertEqual(public_key['kty'], 'EC')
        self.assertEqual(public_key['use'], 'sig')
        self.assertEqual(public_key['crv'], 'secp256k1')
        self.assertEqual(public_key['kid'], self.mykey)


if __name__ == '__main__':
    unittest.main()
