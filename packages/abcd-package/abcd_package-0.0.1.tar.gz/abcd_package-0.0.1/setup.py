import setuptools

setuptools.setup(
    name="abcd_package",
    version="0.0.1",
    author="sirui",
    author_email="siruijhu@gail.com",
    description="A small example package",
    long_description="A small example package",
    long_description_content_type="text/markdown",
    url="https://github.com/SSRRBB/sample_package",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
