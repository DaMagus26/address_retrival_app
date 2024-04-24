import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="legal-bot",
    version="0.0.1",
    description="A chat bot for legal consulting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
