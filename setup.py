from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="my-python-project",
    version="1.0.0",
    author="Your Name",
    author_email="your@email.com",
    description="A Python project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/my-python-project",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # Add your project dependencies here
    ],
)