from setuptools import setup, find_packages

setup(
    name="data-analysis-toolkit",
    version="1.0.0",
    author="Sakineh Dehghan",
    author_email="stats.data.official@gmail.com",
    description="Statistical data analysis and reporting toolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)
