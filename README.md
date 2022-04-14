# A quantum alternative for standard Python random package

[![PyPI version](https://badge.fury.io/py/true-random.svg)](https://badge.fury.io/py/true-random) ![Licence badge](https://img.shields.io/pypi/l/true-random) ![Python version](https://img.shields.io/pypi/pyversions/true-random)
[![Actions Status](https://github.com/peb-8/true-random/workflows/Build%20&%20Test/badge.svg)](https://github.com/peb-8/true-random/actions)
![Dependencies](https://img.shields.io/badge/dependencies-quantumrandom-yellowgreen)
![Downloads per month](https://img.shields.io/pypi/dm/true-random)
![Last commit](https://img.shields.io/github/last-commit/peb-8/true-random)

## Installation : `pip install true-random`

## Features :
- true_randint
- true_choice
- true_shuffle
- true_password

## Generate a strong password :
```python
from truerandom import true_password

print(true_password(length=12))
```
`output : Jjr1i[h*vtsq`

## Generate a bunch of passwords :

```
python -m truerandom --length=12 --nb=100
```

You can also provide a 'csv' param to export the output as a csv file, but it is not recommended to store your passwords on a storage (for security reasons).
