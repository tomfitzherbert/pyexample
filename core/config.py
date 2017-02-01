#!/usr/bin/env python
"""A helper module to enable easier import of the environment variables by
other modules in the project.
"""

import yaml

with open("config.yaml", "r") as f:
    settings = yaml.load(f)
