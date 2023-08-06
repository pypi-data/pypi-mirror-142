import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cjdlib",
    version="1.0.7",
    author="dede",
    author_email="chenjunde_2020@qq.com",
    description="学而思编程社区陈峻德的库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dede-a/cjdlib",
    include_package_data=True,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5"
)
