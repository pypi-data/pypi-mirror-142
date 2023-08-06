from enum import Enum
from os import getcwd
from os.path import exists 
from requests import get

from numpy import loadtxt

from ffast.preprocessor import PreprocessingPipeline

def download_file(url:str,path:str) -> None:
    if exists(path):
        return
    result = get(url)
    if result.ok:
        with open(path,'w') as vector_file:
            vector_file.write(result.text)

PREPROCESSOR = PreprocessingPipeline()
METAPHONES = "ABCEFHIJKLMNOPRSTUWXY0. "
SIZE_METAPHONES = len(METAPHONES)
HERE = getcwd()
PATH = f"{HERE}/poincare.txt"
download_file(path=PATH,url="https://raw.githubusercontent.com/mohammedterryjack/Joint-Intent-Slots/master/word_vectors/poincare.txt")
raw_vocab = loadtxt(PATH,usecols=0,dtype=str)
VOCABULARY = list(map(PREPROCESSOR.normalise,raw_vocab))
VECTORS = loadtxt(PATH,usecols=range(1,101))

class Poincare(Enum):
    SIZE_VECTOR = 100
    SIZE_VOCABULARY = len(VOCABULARY)
    UNKNOWN = "<Unknown>"
    SKIP = "skip"