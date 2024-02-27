build:
python setup.py sdist bdist_wheel

Install:
pip3 install ./dist/ft_package-0.0.1.tar.gz

Display:
pip3 show -v ft_package

Test:
python tester.py

Uninstall
pip3 uninstall ft_package
