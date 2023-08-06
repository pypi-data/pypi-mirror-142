# push the code to gitlab
# inside gitlab add a new tag for the code and update the download URL in setup.py

# reference: https://medium.com/@joel.barmettler/how-to-upload-your-python-package-to-pypi-65edc5fe9c56

python setup.py sdist
twine upload dist/*
