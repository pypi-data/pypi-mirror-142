import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="frag-decorators",
    version="0.0.1",
    author="FQY",
    author_email="qingyun-feng@qq.com",
    description="Some simple but useful decorators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FQY7",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
