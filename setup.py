from setuptools import setup, find_packages

classifiers=[
    "Development Status :: 3 - Alpha",
    "Operating System :: OS Independent",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.7",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
]

setup(
    name="visionner",
    version="0.0.5",
    description="Visionner is a image dataset  toolkit",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type='text/markdown',
    url="https://charleslf2.github.io/Visionner/",
    project_urls={
        "Bug Tracker":"https://github.com/charleslf2/Visionner/issues",
        "Docs":"https://github.com/charleslf2/Visionner",
    },
    author="Charles TCHANAKE",
    author_email="datadevfernolf@gmail.com",
    license="Apache License 2.0",
    keywords=["AI", "Computer vision", "Data centric", "dataset", "images","visualization"],
    classifiers=classifiers,
    install_requires=["numpy", "opencv-python", "matplotlib", "rich"],
    packages=find_packages()
)