#!/usr/bin/env python

"""
 Module
     setup.py
 Copyright
     Copyright (C) 2022 OxyCom Ltd <jamie@oxycom.co.uk>
"""

#from distutils.core import setup, Extension

from setuptools import setup, Extension, find_packages
import numpy as np
import os
import platform
import sys

__version__ = '1.0.6'

# CFLAGS etc
extra_compile_args = []

# Get the target platform
LINUX= platform.system() == 'Linux'
WIN= platform.system() == 'Windows'

if LINUX:
    extra_compile_args.append("-DLINUX")
elif WIN:
    extra_compile_args.append("-DWIN")

# header includes in Manifest.in src/*.h
speechy_module = Extension('_speechy',
                           sources=['speechy_wrap.c', 'src/OxyCoreLib_api.cpp', 'src/Decoder.cpp', 'src/DecoderAllMultiToneMode.cpp', 'src/DecoderAudibleMode.cpp', 'src/DecoderAudibleMultiToneMode.cpp', 'src/DecoderCompressionMultiToneMode.cpp', 'src/DecoderCustomMultiToneMode.cpp', 'src/DecoderNonAudibleMode.cpp', 'src/DecoderNonAudibleMultiToneMode.cpp', 'src/Encoder.cpp', 'src/EncoderAudibleMode.cpp', 'src/EncoderAudibleMultiToneMode.cpp', 'src/EncoderCompressionMultiToneMode.cpp', 'src/EncoderCustomMultiToneMode.cpp', 'src/EncoderNonAudibleMode.cpp', 'src/EncoderNonAudibleMultiToneMode.cpp', 'src/Globals.cpp', 'src/ReedSolomon.cpp', 'src/SpectralAnalysis.cpp'],
                           include_dirs=[np.get_include()],
                           extra_compile_args = extra_compile_args,
                        )
# Required libs
# sudo apt-get install python3-pip && python3-pyaudio

# Meta data
setup (name = 'speechy',
       version=__version__,
       author      = "Speechy",
       author_email="""support@oxycom.co.uk""",
       description = """Speechy Python SDK""",
       long_description="""Python SDK enables the user to send and receive data using the device’s microphone and speaker.""",
       license='License :: Other/Proprietary License',
       ext_modules = [speechy_module],
       install_requires=[
       'pyaudio', 'numpy',
       ],
       py_modules = ["speechy"],
       packages=find_packages(),
       )
