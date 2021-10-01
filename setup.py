from setuptools import setup, find_packages
import toml

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def get_install_requirements():
    try:
        with open ('Pipfile', 'r') as fh:
            pipfile = fh.read()
        pipfile_toml = toml.loads(pipfile)
    except FileNotFoundError:
        return []

    try:
        required_packages = pipfile_toml['packages'].items()
    except KeyError:
        return []

    return ["{0}{1}".format(pkg,ver) if ver != "*"
            else pkg for pkg,ver in required_packages]

setup(
    name = 'cppt',
    version = '0.1.0',
    author = 'Segment Fault',
    # author_email = 'john.doe@foo.com',
    license = 'MIT',
    description = 'A simple command line tool which help you automate your Competitive Programming workflow while still keeping your work directory organised.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = 'https://github.com/vishalagrawal22/CPPT',
    py_modules = ['cppt', 'app'],
    packages = find_packages(),
    install_requires = get_install_requirements(),
    python_requires='>=3.7',
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent",
    ],
    scripts=['cppt'],
)