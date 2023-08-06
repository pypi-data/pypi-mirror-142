from setuptools import setup, find_packages

setup(
    name='simpcfg',
    version='0.2.2',
    description='Simple Configuration Manager',
    url='https://github.com/StephenMal/simpcfg',
    author='Stephen Maldonado',
    author_email='simpcfg@stephenmal.com',
    packages=find_packages(),
    install_requires=['simplogger==0.2.3'],
    classifiers=[
        'Development Status :: 1 - Planning',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities'
    ]
)
