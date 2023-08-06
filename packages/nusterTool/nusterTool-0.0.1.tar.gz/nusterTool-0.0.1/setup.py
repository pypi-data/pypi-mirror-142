from setuptools import setup, find_packages

setup(
    name = "nusterTool",
    version = "0.0.1",
    keywords = ("pip", "toolkit"),
    description = "This is a toolkit for nuster.",
    long_description = "This is a toolkit for nuster.",
    license = "MIT Licence",

    url = "https://github.com/nuster1128/nusterTool.git",
    author = "Nuster",
    author_email = "wfzhangzeyu@163.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    install_requires = []
)