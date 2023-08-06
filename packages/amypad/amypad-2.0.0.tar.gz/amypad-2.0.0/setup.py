from io import open as io_open
import os
from setuptools import setup, find_packages

src_dir = os.path.abspath(os.path.dirname(__file__))
README_rst = ''
fndoc = os.path.join(src_dir, 'README.rst')
with io_open(fndoc, mode='r', encoding='utf-8') as fd:
    README_rst = fd.read()
setup(
    name='amypad',
    version='2.0.0',
    description='Alias for amypet',
    long_description=README_rst,
    long_description_content_type='text/x-rst',
    license='MPL 2.0',
    url='https://github.com/AMYPAD/AmyPET',
    maintainer='Casper da Costa-Luis',
    maintainer_email='casper.dcl@physics.org',
    platforms=['any'],
    install_requires=['amypet'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
    ],
    keywords='pet alzheimers',
)
