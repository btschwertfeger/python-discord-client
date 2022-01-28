
#!/usr/bin/python3
# -*- coding:utf-8 -*-

from setuptools import setup


setup(
    name="pydisco_client",
    version="v0.5.0",
    packages=["client"],
    license="MIT",
    author="Benjamint Thomas Schwertfeger",
    author_email="@b-schwertfeger.de",
    url="https://github.com/btschwertfeger/python-discord-client",
    description="python-discord-client",
    install_requires=["requests", "websockets", "asyncio"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)