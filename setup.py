from setuptools import setup, find_packages

setup(
    name="data-analysis-toolkit",
    version="1.0.1",
    author="Sakineh Dehghan",
    author_email="Sa_dehghan@Sbu.ac.ir",
    description="Statistical data analysis and reporting toolkit",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.8",
)
