from setuptools import setup, find_packages

setup(
    name="dab_project",
    version="0.0.1",
    description="This contains code in ./src directory of the project",
    author="Bharath_Kalluru",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=["setuptools"],
    entry_points={
        "console_scripts": [
            "main=dab_project.main:main"
        ]
    }
)