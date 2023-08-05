import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dataito",
    version="1.0.2",
    author="CAIWEI",
    author_email="caiwei-email@qq.com",
    description="Python data input (i), transform (t), output (o), a line of code to read / convert a variety of formats of data files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ChoiNgai/dataito",
    project_urls={
        "Bug Tracker": "https://github.com/ChoiNgai/dataito/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)