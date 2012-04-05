import ez_setup
ez_setup.use_setuptools()
from setuptools import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import sys
import os
import numpy

if 'setuptools.extension' in sys.modules:
    m = sys.modules['setuptools.extension']
    m.Extension.__dict__ = m._Extension.__dict__

version_py = os.path.join(os.path.dirname(__file__), 'metaseq', 'version.py')
version = open(version_py).read().split('=')[-1].strip().replace('"','')

exts = [Extension(
            'metaseq.rebin',
            ['metaseq/rebin.pyx'],
            include_dirs=[numpy.get_include()])]

long_description = ""
setup(
        name='metaseq',
        version=version,
        cmdclass = {'build_ext': build_ext},
        ext_modules=exts,
        install_requires=['bx-python', 'numpy', 'HTSeq', 'matplotlib', 'scipy', 'scikits.learn', 'pybedtools', 'gffutils'],
        packages=['metaseq', 'metaseq.test', 'metaseq.test.data'],
        package_data={'metaseq':['test/data/*']},
        author_email='dalerr@niddk.nih.gov',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Topic :: Scientific/Engineering :: Bio-Informatics']
    )
