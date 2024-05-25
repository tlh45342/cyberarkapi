all:
	python setup.py bdist_wheel

clean:
	rm -rf build 
	rm -rf cyberarkapi.egg-info 
	rm -rf dist
	pip uninstall -y cyberarkapi

install:
	pip install dist\cyberarkapi-0.1-py3-none-any.whl
