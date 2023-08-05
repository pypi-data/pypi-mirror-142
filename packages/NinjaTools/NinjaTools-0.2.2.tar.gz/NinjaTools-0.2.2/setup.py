import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NinjaTools",
    version="0.2.2",
    author="Nikko Gonzales",
    author_email="nikkoxgonzales@gmail.com",
    description="Bunch of useful tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nikkoxgonzales/ninja-tools",
    install_requires=[
        'pywin32>=303',
        'numpy>=1.22.3',
        'opencv-python==4.5.5.62',
        'scikit-image>=0.19.2'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.9'
)
