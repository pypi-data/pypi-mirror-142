import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tuuid",
    version="1.0",
    author="Montel Edwards",
    author_email="m@monteledwards.com",
    description="Generate unique time-based identifers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/monty-dev/tuuid",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
