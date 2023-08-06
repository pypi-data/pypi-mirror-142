from setuptools import setup

setup(
    name="reisinger_drive",
    packages=["reisingerdrive"],
    install_requires=["aiohttp>=3.0.6", "async_timeout>=3.0.0"],
    version="0.2.0",
    description="A python3 library to communicate with a Reisinger Drive System",
    python_requires=">=3.5.3",
    author="Manni",
    author_email="",
    url="https://github.com/mannipulator/reisingerdrive",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Home Automation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)