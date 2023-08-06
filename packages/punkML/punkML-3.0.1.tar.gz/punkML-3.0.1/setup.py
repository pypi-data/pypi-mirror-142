from setuptools import setup, find_packages


with open('README.rst') as fp:
    long_description = fp.read()
setup(
    name="punkML",

    version="3.0.1",

    description="Primitives for Uncovering New Knowledge.",
    long_description=long_description,

    url="https://gitlab.com/datadrivendiscovery/contrib/punk",

    author="New Knowledge",
    author_email="support@newknowledge.io",

    license="MIT",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",

        # Pick your license as you wish (should match "license" above)
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3.6",

        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],

    keywords=["TA1 primitive", "feature selection", "novelty detection"],

    packages=find_packages(exclude=['tests']),

    install_requires=["numpy", "scikit-learn", "scipy", "pandas", "python-dateutil"],
)
