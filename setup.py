from kudapy import version
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="kudapy",
    version="2.0",
    author=version.__author__,
    author_email="daleentontech@gmail.com",
    description="Python wrapper for making secure requests to Kuda API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/daleentontech/kudapy",
    packages=setuptools.find_packages(),
    install_requires=['requests', 'pycryptodome'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    project_urls={
        'Source': 'https://github.com/daleentontech/kudapy/',
    },
)