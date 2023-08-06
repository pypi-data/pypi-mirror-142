

`proxycalc` does basic Mathematical operations on real numbers.


## Installation

```sh
pip install proxycalc
```

## Usage

Define new Calculator:

```python
>>> from proxycalc import Calculator
>>> calculator = Calculator()
>>> calculator.value
0
```

Find sum of 4 numbers:

```python
>>> from proxycalc import Calculator
>>> calculator = Calculator()
>>> calculator.add(2, 5, 3, 4)
>>> calculator.value
14
```

Subtract 2 numbers from the value:

```python
>>> calculator.subtract(5, 3)
>>> calculator.value
6
```

Multiply value by a number:

```python
>>> calculator.multiply_by(3)
>>> calculator.value
18
```

Divide value by a number:

```python
>>> calculator.divide_by(2)
>>> calculator.value
9
```

Find nth root of result:

```python
>>> calculator.find_root(2)
>>> calculator.value
3
```

Reset calculator:

```python
>>> calculator.reset())
>>> calculator.value
0
```

## Development setup

```sh
$ python3 -m venv env
$ . env/bin/activate
$ make deps
$ tox
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Make sure to add or update tests as appropriate.

Use [Black](https://black.readthedocs.io/en/stable/) for code formatting and [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0-beta.4/) for commit messages.

## [Changelog](CHANGELOG.md)

## License

[MIT](https://choosealicense.com/licenses/mit/)
