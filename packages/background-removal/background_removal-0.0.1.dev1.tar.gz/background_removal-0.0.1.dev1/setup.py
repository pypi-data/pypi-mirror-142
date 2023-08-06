from setuptools import find_packages
from setuptools import setup

with open("README.md") as f:
    long_description = f.read()

setup(
    name="background_removal",
    version="0.0.1dev1",
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Topic :: Artistic Software",
        "Topic :: Multimedia",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Multimedia :: Sound/Audio :: Editors",
        "Topic :: Software Development :: Libraries",
    ],
    description="Remove background from images or videos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Diksha Meghwal",
    author_email="diksha@descript.com",
    url="https://github.com/descriptinc/background-removal",
    license="MIT",
    packages=find_packages(),
    keywords=["video", "image", "matting", "background", "removal", "background removal", "video matting", "image matting"],
    install_requires=[
        "av",
        "pims",
        "tqdm",
    ],

)
