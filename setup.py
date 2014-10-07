from setuptools import setup

setup(
    name="NLGServ",
    version="0.0.0",
    author="Darren Richardson",
    packages=["nlgserv","nlgserv.tests"],
    package_data={"nlgserv":["simplenlg.jar","jython.jar"]},
    scripts=[],
    license="LICENSE.txt",
    description="JSON HTTP wrapper for SimpleNLG",
    long_description=open("README.md").read()
)
