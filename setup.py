from distutils.core import setup

setup(
    name="livecover",
    packages=["livecover"],
    version="0.0.2",
    license="BSD",
    description="Python library to report live code usage",
    author="Rafal Stapinski",
    author_email="stapinskirafal@gmail.com",
    url="https://github.com/rafalstapinski/livecover-py",
    download_url="https://github.com/rafalstapinski/livecover-py/archive/0.0.2.tar.gz",
    keywords=["live", "code", "coverage",],
    install_requires=["coverage==5.2"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
    ],
)
