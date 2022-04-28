import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='omnissiah-utilities',
    version='0.0.1',
    author='Marcin Zelasko',
    author_email='marcin.zelasko@icloud.com',
    description='Testing installation of Package',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/zelaskov/omnissiah-utilities',
    project_urls = {
        "Bug Tracker": "https://github.com/zelaskov/omnissiah-utilities/issues"
    },
    license='MIT',
    packages=['omnissiah-utilities'],
    install_requires=['pyfiglet','PyInquirer'],
)
