# ffast
Fast and lightweight NLP pipeline for ML tasks: powerful tokeniser and (model-free) sentence embeddings using Fast Fourier transforms, power means and Wordnet or Poincare Embeddings

![](images/wordnet.png)
![](images/poincare.jpeg)

## Installation
`pip install ffast`

## Example
```python
from ffast import load

tokeniser = load() #wordnet version (more features)
tokeniser = load("poincare") #poincare version (smaller vectors)
```

see `examples.ipynb` to see what you can do!

## Changelog
- 0.1.0 poincare model introduced alongside wordnet base model to allow for smaller vectors
- 0.0.4 dot similarity implemented to compare batch more efficiently
- 0.0.3 nltk dependencies load bug fixed
- 0.0.2 scipy load bug fixed
- 0.0.1 Initial release