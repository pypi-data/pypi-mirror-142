import os
from setuptools import setup, find_packages

setup(
    name='Neodict2XML',
    version=os.environ['CI_COMMIT_BRANCH'],
    description='Templating utilities',
    long_description=open('README.md').read()+'\n\n\n'+open('CHANGELOG.md').read(),
    long_description_content_type='text/markdown',
    url='https://gitlab.com/kaeraspace/Kaera_Test_Group/Neodict2XML',
    author='Emmanuel Pluot',
    author_email='emmanuel.pluot@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pyyaml',
        'jinja2'
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: Unix',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'License :: OSI Approved :: MIT License',
    ]
)