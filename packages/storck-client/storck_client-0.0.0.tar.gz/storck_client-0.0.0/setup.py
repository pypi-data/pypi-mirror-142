import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
with open('requirements.txt') as f:
    required = f.read().splitlines()

setuptools.setup(
    name="storck_client",
    author_email="mmajewsk@cern.ch",
    description="A client library for storck database system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.cern.ch/velo-calibration-software/storck_client",
    project_urls={
        "Bug Tracker": "https://gitlab.cern.ch/velo-calibration-software/storck_client/-/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    # package_dir={"": "storck_client"},
    py_modules = ['storck_client', '__main__'],

    # entry_points={
    #                     'console_scripts': [
    #                             'storck-client=__main__',
    #                     ]
    #             },
    # packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=required,


)
