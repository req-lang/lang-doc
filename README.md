# req Language documentation

This package contains the sources for the documentation website of the req language.

## How to use

### Install dependencies

```
$ pip install --user -r requirements.txt
```

### Build documentation

You can simply use the `Makefile`

```
$ make html
```

In Windows

```
PS> ./make.bat
```

Or you can use the `sphinx-build`

```
$ sphinx-build -M html ./source ./build
```

**Notes**

- You might have to create the `build` directory if it is the first time you run the build
- You can change the builder from `html` to anything else supported by sphinx

### Develop documentation

To benefit from hot reload use `sphinx-autobuild`:

```
$ sphinx-autobuild ./source ./build
```

Copyright (c), all rights reserved Sami Dahoux 2021-2026
