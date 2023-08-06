import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as file:
    reqs=file.read()
    
reqs=reqs.split("\n")

setuptools.setup(
    name="utils-whitetail",
    version="0.0.8",
    author="Ankesh Gautam",
    author_email="ankesh.gautam@whitetail.in",
    description="Common utils",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/mediblock/lib-web-scrape-utils/",
    project_urls={
        "Bug Tracker": "https://bitbucket.org/mediblock/lib-web-scrape-utils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=reqs,
    python_requires=">=3.6",
)