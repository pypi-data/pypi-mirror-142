import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="codemaoLang",
    version="1.1.0",
    author="BT.Q",
    author_email="BT.Q@qq.com",
    description="一个为编程猫api打造的高度包装的Python库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MinesomeBTQ/CodemaoLang",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
)
