# Indonesia Name and Address Preprocessor

[![pypi](https://img.shields.io/pypi/v/nama_alamat.svg)](https://pypi.org/project/nama_alamat/)
[![python](https://img.shields.io/pypi/pyversions/nama_alamat.svg)](https://pypi.org/project/nama_alamat/)
[![Build Status](https://github.com/kloworizer/nama_alamat/actions/workflows/dev.yml/badge.svg)](https://github.com/kloworizer/nama_alamat/actions/workflows/dev.yml)
[![codecov](https://codecov.io/gh/kloworizer/nama_alamat/branch/main/graphs/badge.svg)](https://codecov.io/github/kloworizer/nama_alamat)

Indonesia Name and Address Preprocessor

-   Documentation: <https://kloworizer.github.io/nama_alamat>
-   GitHub: <https://github.com/kloworizer/nama_alamat>
-   PyPI: <https://pypi.org/project/nama_alamat/>
-   Free software: MIT

## Features

-   Preprocessing Indonesia name and address.

## Instalation

```
pip install nama-alamat
```

## Usage

example of name preproccesing:
```
from nama_alamat.preprocessing import Preprocessing
preprocessing_nama = Preprocessing(tipe='nama')
strings = 'IR SULAEMAN'
print(preprocessing_nama.preprocessing(strings))
```

address preproccesing:
```
from nama_alamat.preprocessing import Preprocessing
preprocessing_alamat = Preprocessing(tipe='alamat')
strings = 'JALAN GARUDA IX BLOK C/3 RT 003 RW 002, JAKARTA UTARA, DKI JAKARTA 12110'
print(preprocessing_alamat.preprocessing(strings))
```

## Credits

This package was created with [Cookiecutter](https://github.com/audreyr/cookiecutter) and the [waynerv/cookiecutter-pypackage](https://github.com/waynerv/cookiecutter-pypackage) project template.
