import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nubecitast",
    version="0.0.2",
    author="Sebastian Tobar Quintero",
    author_email="sebastianq@javerianacali.edu.co",
    description="Libreria para conectarse a servidor de 'Proyecto_nubecita'",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sebastiantq/nubecita",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
