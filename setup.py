from setuptools import setup, find_packages

setup(
    name="GitRepoScraper",
    version="0.1.0",
    author="Guilherme Bernardo",
    author_email="gui25ber@gmail.com",
    description="Embark on a coding quest to map the treasures of GitHub repositories into structured lore.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gui25/GitRepoScraper",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "gitrepotree_scraper=GitRepoScraper.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
