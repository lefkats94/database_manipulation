from setuptools import setup, find_packages

# Read dependencies from requirements.txt
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="Database Manipulation",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    author="Eleftherios Katsikis",
    author_email="ekatsikis@heron.gr",
    description="Database Manipulation Package",
    url="https://github.com/lefkats94/database_manipulation",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
