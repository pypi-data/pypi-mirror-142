"""
BizPy - A framework for developing biz systems by Python.

Only for testing now!

Only for testing now!

Only for testing now!

"""


from setuptools import find_packages, setup


setup(
    name="bizpy",
    version="0.0.1.2022.314 beta",
    author="EGOPY",
    author_email="",
    license="BSD",
    url="https://pypi.org/project/bizpy",
    description="A framework for developing fintech systems.",
    long_description=__doc__,
    keywords='quant investment quantitative trading algotrading',
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.8",
    package_data={"": [
        "*.ico",
        "*.ini",
        "*.dll",
        "*.so",
        "*.pyd",
    ]},
    classifiers=[
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python",
        "Programming Language :: Cython",
        "Programming Language :: C",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Mathematics",
        "License :: OSI Approved :: BSD License"
    ]
)
