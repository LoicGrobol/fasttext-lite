Changelog
=========

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to
[Semantic Versioning](http://semver.org/).

## [Unreleased]

## Added

- Vocabularies are now kept at high level in `fasttextlt.fasttext.FastTextVocab`, which allows you
  to save and load them independently if you're keeping the weights somewhere else and are just
  interested in getting the (sub)word ids.

## Changed

- We now assume [standard
  sizes](https://docs.python.org/3/library/struct.html#byte-order-size-and-alignment) and
  little-endianness when loading a model and enforce it on save.

## [0.1.0] - 2025-05-31

- Initial release.