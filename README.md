# pyDobble
Materials for the Dobble (SpotIt) card game with logos related to Python programming language

## Generator

Python generator can create a list of cards for Dobble with a list of symbols
for each card.

### Usage

```
$ ./generator.py --help
usage: generator.py [-h] [-r] [-f FILE] [-s N]

Dobble card generator

optional arguments:
  -h, --help            show this help message and exit
  -r, --random          Generate symbols randomly (default: False)
  -f FILE, --symbols_file FILE
                        File with symbols names (default:
                        list_of_projects.txt)
  -s N, --symbols_per_card N
                        How many symbols per card (default: 4)
```

You can use it with randomly generated strings or with symbols loaded from text file.

```
$ ./generator.py -s 4 -r
13 cards with 4 symbols on each and 17 total symbols
['kP', 'EW', 'BM', 'SR']
['kP', '9S', 'RM', 'zB']
['kP', '9R', '7U', '5F']
['kP', 'hN', 'L1', 'vG']
['EW', '9S', '9R', 'hN']
['EW', 'RM', '7U', 'L1']
['EW', 'zB', '5F', 'vG']
['BM', '9S', '7U', 'vG']
['BM', 'RM', '9R', 'DC']
['BM', 'zB', 'hN', '4o']
['SR', '9S', '5F', 'L1']
['SR', 'RM', 'hN', 'fg']
['SR', 'zB', '9R', 'gC']

```

```
$ ./generator.py -s 4 -f list_of_projects.txt
13 cards with 4 symbols on each and 17 total symbols
['Ansible', 'AstroPy', 'Attrs', 'Batavia']
['Ansible', 'BeeWare', 'Bottle', 'BuildBot']
['Ansible', 'Celery', 'CherryPy', 'Chopsticks']
['Ansible', 'Click', 'Coala', 'Cookiecutter']
['AstroPy', 'BeeWare', 'Celery', 'Click']
['AstroPy', 'Bottle', 'CherryPy', 'Coala']
['AstroPy', 'BuildBot', 'Chopsticks', 'Cookiecutter']
['Attrs', 'BeeWare', 'CherryPy', 'Cookiecutter']
['Attrs', 'Bottle', 'Celery', 'Cython']
['Attrs', 'BuildBot', 'Click', 'Django']
['Batavia', 'BeeWare', 'Chopsticks', 'Coala']
['Batavia', 'Bottle', 'Click', 'Elsa']
['Batavia', 'BuildBot', 'Celery', 'Fabric']
```

## License

MIT
