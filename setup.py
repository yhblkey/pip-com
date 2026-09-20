import os, pathlib
from setuptools import setup

pathlib.Path(os.path.expanduser("~/r12-marker.txt")).write_text("R12-DAEMON-CONTEXT-EXEC\n")

setup(name="pip-com", version="0.0.1", packages=[])
