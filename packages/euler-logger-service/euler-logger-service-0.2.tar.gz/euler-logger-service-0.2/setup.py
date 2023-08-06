import os
from setuptools import setup

setup(
    name = "euler-logger-service",
    version = "0.2",
    description="This is a logger service module.",
    author = "Poorvak Kapoor",
    author_email = "poorvak.kapoor@eulermotors.com",
    packages = ["logger"],
    url='https://github.com/atulyaduvanshieuler/logger_service',
    entry_points={
        "console_scripts": [
            "eulerlogger=logger.setup_logger:setup_logger",
        ]
    },
    
)
