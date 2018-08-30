# pyDobble
Materials for the Dobble/SpotIt -like card game with logos related to Python programming language

## Generator

Python generator can create a list of cards for Dobble/SpotIt -like game
with a list of symbols for each card.

### Usage

```
$ ./generator.py --help
usage: generator.py [-h] [-r] [-f FILE] [-o N]

Dobble card generator

optional arguments:
  -h, --help            show this help message and exit
  -r, --random          Generate symbols randomly (default: False)
  -f FILE, --symbols_file FILE
                        File with symbols names (default:
                        list_of_projects.txt)
  -o N, --order N       Order of projection [2,3,5,7] (default: 7)
```

You can use it with randomly generated strings or with symbols loaded from text file.

```
$ ./generator.py -o 3
13 cards/symbols with 4 symbols on each
['Ansible', 'AstroPy', 'Attrs', 'BeeWare']
['BeeWare', 'Bottle', 'BuildBot', 'Celery']
['Attrs', 'Bottle', 'CherryPy', 'Chopsticks']
['Ansible', 'Celery', 'Chopsticks', 'Click']
['AstroPy', 'Coala', 'BuildBot', 'Chopsticks']
['AstroPy', 'Cookiecutter', 'CherryPy', 'Celery']
['Attrs', 'Coala', 'Cython', 'Celery']
['BeeWare', 'Cookiecutter', 'Cython', 'Chopsticks']
['AstroPy', 'Bottle', 'Cython', 'Click']
['Attrs', 'Cookiecutter', 'BuildBot', 'Click']
['Ansible', 'CherryPy', 'BuildBot', 'Cython']
['BeeWare', 'Coala', 'CherryPy', 'Click']
['Ansible', 'Cookiecutter', 'Coala', 'Bottle']

```

```
$ ./generator.py -o 2 -r
7 cards/symbols with 3 symbols on each
['Ri', 'f5', '21']
['ER', 's0', 'f5']
['Au', 's0', '21']
['ER', 'Fm', '21']
['Au', 'f5', 'Fm']
['Ri', 's0', 'Fm']
['ER', 'Ri', 'Au']
```

After that, you can use generated JSON output to generate SVG templates
which help you to put right symbols on right cards.

```
$ ./make-svg.py -c 2-output.json 
list 0, card 1, symbol 1, name vJ
list 0, card 1, symbol 2, name QU
list 0, card 1, symbol 3, name Ck
list 0, card 2, symbol 1, name 3D
list 0, card 2, symbol 2, name yS
list 0, card 2, symbol 3, name QU
list 0, card 3, symbol 1, name J2
list 0, card 3, symbol 2, name yS
list 0, card 3, symbol 3, name Ck
list 0, card 4, symbol 1, name 3D
list 0, card 4, symbol 2, name Uy
list 0, card 4, symbol 3, name Ck
list 0, card 5, symbol 1, name J2
list 0, card 5, symbol 2, name QU
list 0, card 5, symbol 3, name Uy
list 0, card 6, symbol 1, name vJ
list 0, card 6, symbol 2, name yS
list 0, card 6, symbol 3, name Uy
list 0, card 7, symbol 1, name 3D
list 0, card 7, symbol 2, name vJ
list 0, card 7, symbol 3, name J2
```

## License

* Generator is licensed under MIT license
* Images in `images` folder have licenses in `images/LICENSES.csv`

## Thanks

* Jyrki Lahtonen for explaining the theory on [math.stackexchange](https://math.stackexchange.com/a/463369/17307)
* Petr Viktorin ([@encukou](https://twitter.com/encukou)) for final generator implementation
