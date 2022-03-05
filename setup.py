from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="harpoon",
    version="0.1.6",
    description="Another OSINT CLI tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Te-k/harpoon",
    author="Tek",
    author_email="tek@randhome.io",
    keywords="osint threatintel",
    include_package_data=True,
    install_requires=[
        "requests",
        "configparser",
        "tweepy>=3.8.0",
        "passivetotal",
        "beautifulsoup4==4.10.0",
        "lxml==4.6.5",
        "censys==2.0.9",
        "shodan",
        "fullcontact.py",
        "pyhunter",
        "PyGitHub",
        "telethon==0.18.3",
        "virustotal-api",
        "pymisp==2.4.134",
        "OTXv2",
        "IPy",
        "maxminddb>=1.4.0",
        "pyasn",
        "spyonweb==0.1",
        "selenium",
        "geoip2",
        "dnspython",
        "consolemd==0.5.1",
        "pypermacc==0.1.1",
        "archiveis",
        "pytz",
        "pypdns==1.3",
        "pybinaryedge==0.5",
        "spyonweb==0.1",
        "pythreatgrid2==0.1.1",
        "pycrtsh==0.3.7",
        "pysafebrowsing==0.1.2",
        "dnsdb==0.2.5",
        "pysecuritytrails==0.1.3",
        "phonenumbers==8.12.4",
        "threatminer==1.0",
        "zetalytics-api==1.0.1",
        "greynoise>=0.8.0",
        "pyhashlookup==1.1.1"
    ],
    python_requires=">=3.5",
    license="GPLv3",
    packages=["harpoon", "harpoon.commands", "harpoon.lib", "harpoon.data"],
    package_dir={"harpoon.lib": "harpoon/lib"},
    package_data={"harpoon": ["harpoon/data/*.conf"]},
    entry_points={"console_scripts": ["harpoon=harpoon.main:main"]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
