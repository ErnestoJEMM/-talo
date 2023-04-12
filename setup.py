from setuptools import find_packages, setup


with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="-talo",
    version="0.0.1",
    author="Ernesto Mart{inez}",
    author_email="A01654795g@tec.com",
    description="Algoritmos de optimización",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ErnestoJEMM/-talo.git",
    install_requires=[
        "numpy>=1.21.6"
    ],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3',
    tests_require=['pytest'],
)