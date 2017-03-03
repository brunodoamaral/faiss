from distutils.core import setup
from os.path import join, exists

if not exists(join("faiss", "_swigfaiss.so")):
    raise Exception("Please go to the root folder and compile Python module first:\n\tmake py")

__version__ = '0.1.0'

setup(
    name='faiss',
    version=__version__,
    description='Faiss is a library for efficient similarity search and clustering of dense vectors.',
    packages=['faiss'],
    package_data={'faiss': ['_swigfaiss.so']},
)
