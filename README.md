# A quantum alternative for standard Python random package


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

## Generate a CSV file of strong passwords :

```
python -m truerandom --csv=output.csv --length=12 --nb=100
```
