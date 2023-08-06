import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="docximg2md", 
    version="0.9.0",
    author="Isabel Sandstrøm",
    author_email="isabel@hermit.no",
    description="Python command line program for taking the images in a word document to markdown",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=['docximg2md'],
    install_requires=['PyPDF2>=1.26.0'],
    entry_points={'console_scripts': ['docximg2md = docximg2md.program:main']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)