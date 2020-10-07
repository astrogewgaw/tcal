import pathlib
import versioneer

from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")

install_requires = ["pyqt5", "pandas", "tabulate", "sqlalchemy"]


setup(
    name="tcal-astro",
    version=versioneer.get_version(),
    description="The Comprehensive Astrochemists' List",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/astrogewgaw/tcal",
    author="Ujjwal Panda",
    author_email="ujjwalpanda97@gmail.com",
    entry_points={
        "console_scripts": ["tcal=tcal.app.tcal:main"],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering :: Astronomy",
    ],
    keywords=("academia, " "astrochemists, " "contact list"),
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    include_package_data=True,
    python_requires=">=3.7, <4",
    install_requires=install_requires,
    project_urls={
        "Source": "https://github.com/astrogewgaw/tcal",
        "Bug Reports": "https://github.com/astrogewgaw/tcal/issues",
    },
    cmd_class=versioneer.get_cmdclass(),
    zip_safe=False,
)
