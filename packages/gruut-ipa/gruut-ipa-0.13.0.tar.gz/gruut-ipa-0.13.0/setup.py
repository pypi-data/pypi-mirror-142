"""Setup file for gruut-ipa"""
from pathlib import Path

import setuptools

this_dir = Path(__file__).parent

# -----------------------------------------------------------------------------

# Load README in as long description
long_description: str = ""
readme_path = this_dir / "README.md"
if readme_path.is_file():
    long_description = readme_path.read_text(encoding="UTF-8")

requirements = []
requirements_path = this_dir / "requirements.txt"
if requirements_path.is_file():
    with open(requirements_path, "r", encoding="utf-8") as requirements_file:
        requirements = requirements_file.read().splitlines()

version_path = this_dir / "VERSION"
with open(version_path, "r", encoding="utf-8") as version_file:
    version = version_file.read().strip()

# -----------------------------------------------------------------------------

module_dir = this_dir / "gruut_ipa"
data_dir = module_dir / "data"
data_files = [str(f.relative_to(module_dir)) for f in data_dir.rglob("*")]

setuptools.setup(
    name="gruut-ipa",
    description="Library for manipulating pronunciations using the International Phonetic Alphabet (IPA)",
    version=version,
    author="Michael Hansen",
    author_email="mike@rhasspy.org",
    url="https://github.com/rhasspy/gruut-ipa",
    packages=setuptools.find_packages(),
    package_data={"gruut_ipa": data_files + ["py.typed"]},
    install_requires=requirements,
    extras_require={':python_version<"3.7"': "dataclasses"},
    entry_points={"console_scripts": ["gruut-ipa = gruut_ipa.__main__:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
)
