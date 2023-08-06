import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Vsvpack",                     # This is the name of the package
    ulr="https://github.com/PackTheCommand/Vsvpack",
    version="0.0.6",                        # The initial release version
    
    author="PackTheCommand",                     # Full name of the author
    description="A package for saving and reading simple Data like Setings",
    long_description = "A package for saving and reading simple Data like Setings",     # Long description read from the the readme file
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages("os","sys"),    # List of all python modules to be installed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      # Information to filter the project on PyPi website
    python_requires='>=3.6',                # Minimum version requirement of the package
    py_modules=["Vsvpack"],             # Name of the python package
    package_dir={'':'Vsvpack/src'},     # Directory of the source code of the package
    install_requires=[]                     # Install other dependencies if any
)





