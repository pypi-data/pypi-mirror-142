import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mkvpy",
    version="0.0.2",
    author="Mateusz Bednarski",
    author_email="msz.bednarski@gmail.com",
    description="Python client for geohot/minikeyvalue key/value store.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    py_modules=["mkvpy"],
    package_dir={'': 'mkvpy/src'},
    requires=["requests"]
)