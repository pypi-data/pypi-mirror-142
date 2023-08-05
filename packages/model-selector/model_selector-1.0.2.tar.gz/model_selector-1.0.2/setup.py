import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="model_selector",
    version="1.0.2",
    author="Harry McNinson",
    author_email="harrymn@uw.edu",
    description="This package will help you select the regression model or classification model for your dataset. "
                "Provide the file path to your dataset and watch this package do the rest of the work for you.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/halculvin/model_selector",
    packages=setuptools.find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)