#!/bin/bash

info() { printf "\n%s %s\n\n" "$( date )" "$*" >&2; }

info "Create the source archive"

python setup.py sdist

info "Create the wheels"

python setup.py bdist_wheel

info "Upload the results to twine"

version=$(python setup.py --version)

twine upload --repository-url https://upload.pypi.org/legacy/ -u michaelsprenger dist/*${version}*
