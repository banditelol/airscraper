import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='airscraper',
    version='0.1.2',
    author="Aditya Rachman Putra",
    author_email="adityarputra@gmail.com",
    description="Airtable Download CSV helper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/banditelol/airscraper",
    packages=setuptools.find_packages(),

    entry_points ={
        'console_scripts': [
            'airscraper = airscraper.airscraper:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'beautifulsoup4',
    ]

 )
