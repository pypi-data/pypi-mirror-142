import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="cmdwatch",
    version="0.0.7",
    author="Karthik E C",
    author_email="eckarthik39@gmail.com",
    description="A CLI tool to watch for command outputs and store them to a file for further analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    entry_points='''
       [console_scripts]
       cmdwatch=cmdwatch.__main__:main
   ''',
    url="https://github.com/eckarthik/cmdwatch",
    keyword="linux, windows, command, cli, watch, execute, repeat, analysis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
    python_requires='>=3.6',
)