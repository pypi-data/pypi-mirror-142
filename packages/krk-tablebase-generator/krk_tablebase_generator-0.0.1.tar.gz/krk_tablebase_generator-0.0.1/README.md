# KRK Tablebase Generator

KRK Tablebase Generator is a C++ extension for accelerating the generation of a [King and Rook versus King](https://www.chessprogramming.org/KRK) (KRK) endgame tablebase.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install krk-tablebase-generator.

```bash
pip install krk-tablebase-generator
```

## Usage

```python
import tablebase

# returns a tuple containing black to move positions and white to move positions
tablebase.get_lists()
```

## License
[MIT](https://choosealicense.com/licenses/mit/)