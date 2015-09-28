#!/usr/bin/env python

"""
Clean up generated files.
"""

import os

import breakthrough

for basename in os.listdir(breakthrough.image_dir):
    path = os.path.join(breakthrough.image_dir, basename)
    if (os.path.isfile(path)
            and (path.endswith(breakthrough.output_suffix)
            or path.endswith(breakthrough.intermediate_suffix))):
        os.unlink(path)

