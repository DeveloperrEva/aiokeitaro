from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

setup(
    name='aiokeitaro',
    version='1.0.2',
    packages=find_packages(exclude=['tests']),
    install_requires=['aiohttp'],
    package_data={
        '': ['*.py']
    },
    author='Developereva',
    author_email='developereva@protonmail.com',
    description='Unofficial Asynchronous Keitaro Admin API client',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/developerreva/aiokeitaro',
    keywords='python python3 api-client aiohttp api-wrapper keitaro keitaro-tracker keitaro-async',
    project_urls={
        'Source Code': 'https://github.com/developerreva/aiokeitaro',
        'Documentation': 'https://github.com/developerreva/aiokeitaro#-getting-started',
        'Keitaro Admin API Documentation': 'https://admin-api.docs.keitaro.io/'
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    tests_require=['pytest']
)
