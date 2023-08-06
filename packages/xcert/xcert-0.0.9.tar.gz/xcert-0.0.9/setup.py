import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
if os.environ.get('CI_COMMIT_TAG'):
    version = os.environ['CI_COMMIT_TAG']
else:
    version = os.environ['CI_JOB_ID']

setuptools.setup(
    name="xcert",
    version=version,
    author="Riny Meester",
    author_email="rinini@me.com",
    description="A tool to manage Xolphin certificates",
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    scripts=['xcert'],
    install_requires=['pyOpenSSL', 'xolphin-api']
)
