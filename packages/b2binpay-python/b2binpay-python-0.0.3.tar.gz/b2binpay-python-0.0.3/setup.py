import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="b2binpay-python",
    version="0.0.3",
    author="allkap",
    author_email="author@example.com",
    description="Library for working with b2binpay api",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/allkap/b2binpay-py",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["aiohttp==3.8.1",
                      "aiosignal==1.2.0",
                      "async-timeout==4.0.2",
                      "attrs==21.4.0",
                      "certifi==2021.10.8",
                      "charset-normalizer==2.0.12",
                      "frozenlist==1.3.0",
                      "idna==3.3",
                      "loguru==0.6.0",
                      "multidict==6.0.2",
                      "requests==2.27.1",
                      "urllib3==1.26.8",
                      "yarl==1.7.2",
                      "python-dotenv~=0.19.2",
                      "setuptools~=60.9.3"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
