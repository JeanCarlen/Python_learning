from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    url="https://https://github.com/JeanCarlen/\
        Python_learning/ex09/ft_package",
    author="jcarlen",
    author_email="jcarlen@student.42Lausanne.ch",
    description="A sample test package",
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    entry_points={
        'console_scripts': [],
    },
)
