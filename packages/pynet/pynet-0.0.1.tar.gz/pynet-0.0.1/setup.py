from os.path import join
from os.path import dirname

from setuptools import find_packages
from setuptools import setup


def read_version():
    version_contents = {}
    with open(join(dirname(__file__), 'pynet', 'version.py')) as fh:
        exec(fh.read(), version_contents)

    return version_contents['VERSION']

def load_readme():
    return "pynet Python Library"


INSTALL_REQUIRES = [
]


setup(
    name='pynet',
    version=read_version(),
    description='pynet Python Library',
    long_description=load_readme(),
    long_description_content_type='text/markdown',
    author='CodeMax',
    author_email='istommao@gmail.com',
    url='https://github.com/istommao/pynet',
    license='MIT',
    keywords='pynet python network sdk',
    packages=find_packages(
        exclude=[
            'tests',
            'tests.*',
            'testing',
            'testing.*',
            'virtualenv_run',
            'virtualenv_run.*',
        ],
    ),
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    python_requires='>=3.6',
    project_urls={
        'Website': 'https://github.com/istommao/pynet',
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)