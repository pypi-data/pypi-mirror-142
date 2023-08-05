from setuptools import setup, find_packages

def parse_requirements():
    """ load requirements from a pip requirements file """
    lineiter = (line.strip() for line in open("requirements.txt"))
    return [line for line in lineiter if line and not line.startswith("#")]
    
install_reqs = parse_requirements()

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="alectiolite",
    version="0.0.1",
    author="Alectio",
    author_email="admin@alectio.com",
    url='https://github.com/alectio/alectio-lite',
    description="Integrate customer side ML application with the Alectio Platform",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=["tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Logging',
        'Topic :: System :: Monitoring'
    ],
    python_requires=">=3.6",
    install_requires=install_reqs,
    package_data={"": ["alectiolite"]},
    include_package_data=True,
)
