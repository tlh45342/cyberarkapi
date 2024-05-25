
## CYPERARKAPI 

Look for other implementations probably before using this.  This is what I created
and is usable for my own use.

## Requirements

I would hazard to guess that it is probably unlikely that you do not already have the following modules, but on the off chance
this is a new environment you may need to include the following setuptools and requests module.

```bash
pip install -r requests.txt
```

## Makefile Commentary

# windows environment
If using Windows the windows does depend on a a development environment support
 I work with the gnuwin32.sourceforge.net variety.  One would expect the MSYS2 distribution would work fine as well.
 * make
 * rm

# Linux, etc
  I expect you will want build essentials

```bash
apt-get install build-essential
```
  
## Producing the package for the module

The "Package" or wheel can be made using "make"

make clean\
make\
make install

please examine the requirements.txt

## TESTING

The tests directory has a number a few tests.
