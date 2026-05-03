from setuptools import setup, find_packages

setup(
    name="Testing app",
    description="Testing app for learning purposes",
    version="0.1.0",
    packages= find_packages(),
    entry_points={
    "console_scripts":
    ["test_app=setup.test:main"]
    }
)