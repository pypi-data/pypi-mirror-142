
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SHU-cxAutoSign",
    version="0.2.0",
    author="XHLin",
    author_email="xhaughearl@gmail.com",
    description="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    install_requires = [
        'ras',
        'lxml',
        'requests',
        'beautifulsoup4'
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=["SHU_cxAutoSign"],
    python_requires=">=3.6",
)