from distutils.core import setup

setup(
    name="livecover",
    packages=["livecover"],
    version="0.1",
    license="BSD",
    description="TYPE YOUR DESCRIPTION HERE",  # Give a short description about your library
    author="Rafal Stapinski",  # Type in your name
    author_email="stapinskirafal@gmail.com",  # Type in your E-Mail
    url="https://github.com/stapinskirafal/livecover-py",
    keywords=["live", "code", "coverage",],
    install_requires=["coverage==5.2"],  # I get to this in a second
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3.8",
    ],
)
