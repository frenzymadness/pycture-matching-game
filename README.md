# pyDobble
Materials for the Dobble (SpotIt) card game with logos related to Python programming language

## Generator

Python generator can create a list of cards for Dobble with a list of symbols
for each card.

### Usage

```
$ ./combinations-generator.py --help
usage: combinations-generator.py [-h] [-r] [-f FILE] [-n N]

Dobble card generator

optional arguments:
  -h, --help            show this help message and exit
  -r, --random          Generate symbols randomly (default: False)
  -f FILE, --symbols_file FILE
                        File with symbols names (default:
                        list_of_projects.txt)
  -n N, --number N      The prime number to base generator on. (default: 5)
```

You can use it with randomly generated strings or with symbols loaded from text file.

```
$ ./combinations-generator.py  -r -n 3
13 cards/symbols generated. Each card contains 4 symbols
('4p', 'nU', '9v', 'Oh')
('4p', 'F5', 'hZ', 'jE')
('4p', 'kq', 'hb', 'dz')
('4p', 'zj', 'uV', 'nW')
('nU', 'F5', 'kq', 'zj')
('nU', 'hZ', 'hb', 'uV')
('nU', 'jE', 'dz', 'nW')
('9v', 'F5', 'hb', 'nW')
('9v', 'hZ', 'dz', 'zj')
('9v', 'jE', 'kq', 'uV')
('Oh', 'F5', 'dz', 'uV')
('Oh', 'hZ', 'kq', 'nW')
('Oh', 'jE', 'hb', 'zj')
```

```
$ ./combinations-generator.py  -n 3 -f list_of_projects.txt
13 cards/symbols generated. Each card contains 4 symbols
('Click', 'ctypes', 'Django', 'Elsa')
('Click', 'Flask', 'Git', 'Github')
('Click', 'IPython', 'Jinja', 'Jupyter')
('Click', 'Jython', 'Matplotlib', 'MicroPython')
('ctypes', 'Flask', 'IPython', 'Jython')
('ctypes', 'Git', 'Jinja', 'Matplotlib')
('ctypes', 'Github', 'Jupyter', 'MicroPython')
('Django', 'Flask', 'Jinja', 'MicroPython')
('Django', 'Git', 'Jupyter', 'Jython')
('Django', 'Github', 'IPython', 'Matplotlib')
('Elsa', 'Flask', 'Jupyter', 'Matplotlib')
('Elsa', 'Git', 'IPython', 'MicroPython')
('Elsa', 'Github', 'Jinja', 'Jython')
```

## License

MIT
