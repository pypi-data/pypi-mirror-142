import os
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


class CleanCommand(setuptools.Command):
    """ Custom clean command to tidy up the project root. """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('rm -vrf ./build ./dist ./*.pyc ./*.tgz ./*.egg-info')


class PrepublishCommand(setuptools.Command):
    """  Custom prepublish command. """
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        os.system('python setup.py clean')
        os.system('python setup.py sdist bdist_wheel')


setuptools.setup(
    cmdclass={
        'clean': CleanCommand,
        'prepublish': PrepublishCommand,
    },
    name='myeq',
    version='0.0.4',
    url='https://github.com/jmgomezsoriano/myeq',
    license='lGPLv3',
    author='José Manuel Gómez Soriano',
    author_email='jmgomez.soriano@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    description='Some simple useful math equations.',
    packages=setuptools.find_packages(exclude=['test']),
    package_dir={'myeq': 'myeq'},
    include_package_data=False,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[]
)
