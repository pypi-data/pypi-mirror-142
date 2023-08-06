from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'FFAST: Fast Fourier Analysis for Sentence embeddings and Tokenisation'
LONG_DESCRIPTION = 'Fast and lightweight NLP pipeline for ML tasks: powerful tokeniser and (model-free) sentence embeddings using Fast Fourier transforms, power means and Wordnet'

setup(
    name="ffast",
    version=VERSION,
    author="Mohammed Terry-Jack",
    author_email="<mohammedterryjack@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['nltk', 'jellyfish', 'Unidecode', 'numpy', 'scipy'],
    keywords=['python', 'embedding', 'tokenisation', 'fast fourier', 'nlp', 'nlu'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)