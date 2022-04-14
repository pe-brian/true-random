# A quantum alternative for standard Python random package (based on quantumrandom package)


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
