from setuptools import setup

version = "0.0.9"


def get_readme_md_contents():
    """read the contents of your README file"""
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
        return long_description


setup(
    name="livecover",
    packages=["livecover"],
    version=version,
    license="BSD",
    description="The livecover python package",
    long_description=get_readme_md_contents(),
    long_description_content_type="text/markdown",
    author="Rafal Stapinski",
    author_email="stapinskirafal@gmail.com",
    url="https://github.com/rafalstapinski/livecover-py",
    download_url="https://github.com/rafalstapinski/livecover-py/archive/{}.tar.gz".format(
        version
    ),
    keywords=["live code coverage",],
    install_requires=["coverage==5.2"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
    ],
)
