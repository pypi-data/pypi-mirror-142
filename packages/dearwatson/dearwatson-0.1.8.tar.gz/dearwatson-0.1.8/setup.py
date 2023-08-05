import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

version = "0.1.8"
setuptools.setup(
    name="dearwatson", # Replace with your own username
    version=version,
    author="M. Dévora-Pajares",
    author_email="mdevorapajares@protonmail.com",
    description="Visual Vetting and Analysis of Transits from Space ObservatioNs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PlanetHunters/watson",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.8',
    install_requires=[
                        'argparse==1.4.0',
                        'beautifulsoup4==4.9.3',
                        'configparser==5.0.1',
                        "cython==0.29.21",
                        "extension-helpers==0.1",
                        "imageio==2.9.0",
                        "lcbuilder==0.7.15",
                        "matplotlib==3.3.4",
                        'pyparsing==2.4.7', # Matplotlib dependency
                        "pyyaml==5.4.1",
                        "reportlab==3.5.59",
                        'setuptools>=41.0.0',
    ]
)