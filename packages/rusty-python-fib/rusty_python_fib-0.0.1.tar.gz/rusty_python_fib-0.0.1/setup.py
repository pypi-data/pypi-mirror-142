from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="rusty_python_fib",
    version="0.0.1",
    author="Alexander Stenmark",
    author_email="alexstenmark92@gmail.com",
    description="Calculates a fibonacci number",
    long_description=long_description,
    url="https://github.com/ergho/rusty-python-fib",
    install_requires=["PyYAML>=4.1.2", "dill>=0.2.8"],
    packages=find_packages(exclude=("tests",)),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "fib-number = rusty_python_fib.cmd.fib_numb:fib_numb",
        ],
    },
    extras_require={"server": ["Flask>=1.0.0"]},
)
