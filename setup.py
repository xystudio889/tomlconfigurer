from setuptools import setup, find_packages

setup(
    name="tomlconfigurer",
    version="0.1.0.dev0",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=["toml"],
    python_requires=">=3.7",
    author="xystudio",
    author_email="173288240@qq.com",
    description="A configurer with toml.",
    long_description=open("README-PYPI.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/xystudio889/tomlconfigurer",
    entry_points={
            "tomlconfigurer = configurer:main",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    extras_require={
        "dev": []
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
