from setuptools import setup

classifiers = [
    "Development Status :: 1 - Planning",
    "Intended Audience :: Developers",
    "Operating System :: Microsoft :: Windows :: Windows 10",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
]

setup(
    name="hcord-py",
    version="0.0.1.1",
    description="A Discord API Wrapper written in Python.",  # noqa: E501
    long_description=open("README.md").read(),
    url="",
    author="MaskDuck",
    license="MIT",
    classifiers=classifiers,
    keywords="discord",
    packages=["hcord"],
    long_description_content_type="text/markdown",
    install_requires=["aiohttp", "aiodns"],
)
