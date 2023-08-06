from pathlib import Path

from setuptools import find_packages, setup

__location__ = Path(__file__).resolve().parent


setup(
    name="s3000",
    version="0.0.1",
    description="S3000",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 1 - Planning",
    ],
)
