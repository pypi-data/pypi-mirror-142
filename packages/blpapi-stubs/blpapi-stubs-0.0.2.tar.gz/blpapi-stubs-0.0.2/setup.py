from setuptools import setup
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="blpapi-stubs",
    version="0.0.2",
    author="Stiofán Fordham",
    author_email="stiofan.fordham@gmail.com",
    description="Mypy stubs for blpapi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sdfordham/blpapi-stubs",
    project_urls={
        "Bug Tracker": "https://github.com/sdfordham/blpapi-stubs/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["mypy>=0.790", "typing-extensions>=3.7.4"],
    packages=["blpapi"],
    package_data={"": ["*.pyi", "py.typed"]},
)
