import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ndacrawler",
    version="0.0.12",
    author="Antonio Mande",
    author_email="mandetonny@gmail.com",
    description="A simple crawler for the NDA website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AntonioMande/ndacrawler",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src", exclude=['tests*']),
    python_requires=">=3.6",
    install_requires=["requests", "beautifulsoup4==4.10", "lxml"]
)
