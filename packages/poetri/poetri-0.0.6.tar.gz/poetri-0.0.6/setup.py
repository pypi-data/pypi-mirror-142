import os
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name="poetri",
      version="0.0.6",
      description="Pre-OAuth Entity Trust Reference Implementation (POETRI) using secp256k1",
      long_description="""Command line tools and python libraries for creating keys(JWK), and signing/verifying signatures of JWTs.""",
      author="Alan Viars",
      author_email="alan@transparenthealth.org",
      url="https://github.com/transparenthealth/python-poetri",
      download_url="https://github.com/transparenthealth/python-poetri/tarball/master",
      install_requires=['requests', 'jwcrypto'],
      packages= ['poetri', 'tests'],
      scripts=['poetri/verify_jws_with_jwk.py',
               'poetri/verify_jws_with_jwk_url.py',
               'poetri/sign_jwk.py',
               'poetri/generate_jwk_private.py',
               'poetri/generate_jwk_public.py',
               ]
      )

