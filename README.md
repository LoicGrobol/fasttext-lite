FastText lite
=============

[![Latest PyPI version](https://img.shields.io/pypi/v/fasttextlt.svg)](https://pypi.org/project/fasttextlt)
[![Build status](https://github.com/LoicGrobol/fasttextlt/actions/workflows/ci.yml/badge.svg)](https://github.com/LoicGrobol/fasttext-lite/actions/workflows/ci.yml)

A pure[^1] Python FastText model reader, to ensure that FastText model stay usable for as long as
possible.s

**This is slower than the original FastText**, for some methods by orders of magnitude. It's the
price to pay for not using Cython or compiled code. These methods are also not usually bottlenecks
in standard uses of FastText.

FastText has been in maintenance mode for some time, with no indication that it will ever change. In
the absence of further releases, it will stay stuck in increasingly obsolete Python version and get
increasingly hard to rebuild. [Gensim](https://radimrehurek.com/gensim/) has a working
re-implementation that is easier to use, but it too has a relatively slow release pace and does not
necessarily keep up with the rest of the Python ecosystem. This project provides a path to keep
using FastText model for longer and a low cost, by extracting the relevant part from Gensim,
allowing to load FastText models and use for word embeddings purposes in pure Python and be as
future-proof as possible. If you want to train new model, I would advise starting a new library from
scratch to avoid being stuck in FastText's historical cruft, and take inspiration from
[Floret](https://github.com/explosion/floret) instead.

[^1]: The only non-pure Python dependency is NumPy 2, which can reasonably be expected to be
    available.

## Licence

This software is released under the LGPL v2.1 Licence, see [LICENCE.md](LICENCE.md) for the details.
