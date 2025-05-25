#!/usr/bin/env python3
"""
Setup script for the NovelForge AI package.
"""
from setuptools import setup, find_packages
import os

# Read the contents of README.md
with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

# Read the requirements from requirements.txt
with open("requirements.txt", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="novelforge-ai",
    version="0.2.0",
    description="AI-powered publishing platform using Google's Gemini API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Mosaddiq",
    author_email="mosaddiq@example.com",
    maintainer="Mosaddiq",
    url="https://github.com/mosadd1X/novelforge-ai",
    packages=find_packages(),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        "console_scripts": [
            "novelforge-ai=src.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Text Processing :: General",
    ],
    python_requires=">=3.8",
)
