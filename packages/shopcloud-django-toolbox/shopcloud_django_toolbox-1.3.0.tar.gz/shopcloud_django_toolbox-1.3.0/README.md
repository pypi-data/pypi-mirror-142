# Django Toolbox

## install

```sh
$ pip install shopcloud-django-toolbox
```

## deploy

```sh
$ version in setup.py ändern und dann ...
$ pip3 install wheel twine
$ python3 setup.py sdist bdist_wheel
$ twine upload dist/* 
```