import setuptools

with open("README.md", "r") as fh:

    long_description = fh.read()

setuptools.setup(

    name="asif_simple_calc", # Replace with your package name
    version="0.0.1",
    author="Asif Ali Mehmuda",
    author_email="asif.mehmuda9@gmail.com",
    description="A simple educational package to perform basic mathematical calculations",
    long_description= "An educational package to perform addition, subtraction and absolute subtraction of two numbers",
    long_description_content_type="text/markdown",
    url="https://github.com/aliasif1/pypi_simple_calculator.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',

)