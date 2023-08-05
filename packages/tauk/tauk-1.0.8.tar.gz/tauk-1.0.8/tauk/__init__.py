"""Helper package to facilitate reporting for webdriver-based tests on Tauk"""

from tauk.tauk_appium import Tauk

__project__ = "tauk"
__version__ = "1.0.8"
__author__ = "Nathan Krishnan"
__url__ = "https://github.com/thetauk/tauk-webdriver-python"
__platforms__ = "ALL"
__classifiers__ = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]
__requires__ = ["requests", "Appium-Python-Client", "selenium"]

__extra_requires__ = {
}
