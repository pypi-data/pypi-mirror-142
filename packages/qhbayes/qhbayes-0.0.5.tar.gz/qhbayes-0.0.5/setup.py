from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="qhbayes",
    version="0.0.5",
    author="Mark Woodhouse",
    author_email="mark.woodhouse@bristol.ac.uk",
    description="Bayesian methods for inferring mass eruption rate for column height (or vice versa) for volcanic eruptions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://bitbucket.org/markwoodhouse/qhbayes",
    project_urls={
        "Bug Tacker": "https://bitbucket.org/markwoodhouse/qhbayes/admin/issues"
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "qhbayes"},
    packages=find_packages(where="qhbayes"),
    # packages=find_packages(),
    install_requires=[
        "markdown",
        "numpy",
        "scipy",
        "matplotlib",
        "pandas",
        "plotly",
        "dash",
        "dash_bootstrap_components",
        "dash_extensions",
    ],
    include_package_data=True,
)
