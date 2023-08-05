import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="build_duck",
    version="0.0.1",
    author="Cora DeFrancesco",
    author_email="coraanndefran@gmail.com",
    description="Package to create a duck marker in matplotlib.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CoraDeFrancesco/build_duck",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)
