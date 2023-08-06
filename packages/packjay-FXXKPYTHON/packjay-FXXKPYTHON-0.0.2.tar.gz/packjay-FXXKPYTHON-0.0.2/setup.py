import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="packjay-FXXKPYTHON",
    version="0.0.2",
    author="JayChen",
    author_email="12345678@qq.com",
    description="一个测试",
    long_description=long_description,
    url="https://github.com/pypa/sampleproject",
    license="MIT Licence",
    packages=setuptools.find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ],
)
