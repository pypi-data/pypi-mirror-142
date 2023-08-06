import setuptools


with open('README.md', 'r', encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='magento-2-api',
    version='0.1.3',
    author='Dalton Marler',
    author_email='daltonmarler@outlook.com',
    description='A python module for interacting with the Magento 2 REST API.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dmarler/python-magento-2-api',
    project_urls={
        "Bug Tracker": "https://github.com/dmarler/python-magento-2-api/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
    ],
    install_requires=[
        'requests',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
