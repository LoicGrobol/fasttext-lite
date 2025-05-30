FastText lite
=============

[![Latest PyPI
version](https://img.shields.io/pypi/v/fasttextlt.svg)](https://pypi.org/project/fasttextlt)
[![Build
status](https://github.com/LoicGrobol/fasttextlt/actions/workflows/ci.yml/badge.svg)](https://github.com/LoicGrobol/fasttext-lite/actions/workflows/ci.yml)

A pure[^1] Python FastText interface, to ensure that FastText model stay usable for as long as
possible.

- **This is slower than the original FastText**, for some methods by orders of magnitude. It's the
price to pay for not using Cython or compiled code. These methods are also not usually bottlenecks
in standard uses of FastText.
- **Support for training is not planned**, if you want to train new models, I would advise starting
a new library from scratch to avoid being stuck in FastText's historical cruft, and take inspiration
from [Floret](https://github.com/explosion/floret) instead. You can save models using FastText lite,
but you'll have to change the weights etc manually.


FastText has been in maintenance mode for some time, with no indication that it will ever change. In
the absence of further releases, it will stay stuck in increasingly obsolete Python versions and get
increasingly hard to rebuild. [Gensim](https://radimrehurek.com/gensim/) has a working
re-implementation that is easier to use, but it too has a relatively slow release pace and does not
necessarily keep up with the rest of the Python ecosystem. This project provides a path to keep
using FastText models for longer and at low cost, by extracting the relevant parts from Gensim and
converting the Cython parts back to pure Python (and optimising them as well as I can). So far it
supports loading the binary models and use them for word embedding purposes.


[^1]: The only non-pure Python dependency is NumPy 2, which can reasonably be expected to be
    available.

## Licence

This software is released under the LGPL v2.1 Licence, see [LICENCE.md](LICENCE.md) for the details.
