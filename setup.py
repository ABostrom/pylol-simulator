import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pylol_simulator", # Replace with your own username
    version="0.0.1",
    author="Aaron Bostrom",
    author_email="a.bostrom@uea.ac.uk",
    description="A package to simulate damage in the game League of Legends",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/abostrom/pylol-simulator",
    project_urls={
        "Bug Tracker": "https://github.com/abostrom/pylol-simulator/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)