import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tensegrity",
    version="0.0.0",
    author="Baihan Lin",
    author_email="doerlbh@gmail.com",
    description="Python library of tensegrity analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/doerlbh/tensegrity",
    project_urls={
        "Bug Tracker": "https://github.com/doerlbh/tensegrity/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    license="GPLv3",
    package_dir={"": "tensegrity"},
    packages=setuptools.find_packages(where="tensegrity"),
    python_requires=">=3.6",
    install_requires=["numpy>=1.16.5", "pandas"],
    test_suite="nose.collector",
    tests_require=["nose"],
    include_package_data=True,
)
