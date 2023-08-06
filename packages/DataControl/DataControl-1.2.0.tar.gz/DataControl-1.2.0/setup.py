import setuptools

with open("readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="DataControl",
    version="1.2.0",
    author="CAIWEI",
    author_email="caiwei@kuaishou.com",
    description="Data governance script summary",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/xxxxx/datacontrol",
    project_urls={
        "Bug Tracker": "https://github.com/xxxxx/datacontrol/issues",
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