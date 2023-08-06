|docs| |pipelines|

###############################################
Lagranto - A Library to work with trajectories.
###############################################

A recent build of the documentation is available at https://lagranto.readthedocs.io/en/latest/

Changelog
---------

The changelog of can be found under `CHANGELOG.md <CHANGELOG.md>`_.


Install the development environment
-----------------------------------

Copy locally the latest version from lagranto:

.. code-block:: bash

    git clone git@git.iac.ethz.ch:atmosdyn/Lagranto.git /path/to/local/lagranto
    cd path/to/local/lagranto

Prepare the conda environment:

.. code-block:: bash

    module load miniconda3
    conda create -y -q -n lagranto_dev python=3.5.4 pytest
    conda env update -q -f lagranto.yml -n lagranto_dev

Install lagranto in development mode in lagranto_dev:

.. code-block:: bash

    source activate lagranto_dev
    pip install -e .

Run the tests:

.. code-block:: bash

    python -m pytest

Make the modifications available
--------------------------------

.. code-block:: bash

    git clone URL       # Copy the server version locally
    git status          # Give the status of the file as seen from git
    git pull            # Get the latest version from the server
    git add FILES...    # Add modified files
    git commit          # Add the changes to the git system, only locally
    git push            # Push the local changes to the server

Documentation
-------------

To compile the documentation the `sphinx` package have to be installed:

.. code-block:: bash

    conda install sphinx

To compile the html documentation:

.. code-block:: bash

    cd docs
    make html



Update package on conda and PyPi
--------------------------------

Prerequisites
~~~~~~~~~~~~~

Conda
=====

- A github account
- Fork the repository https://github.com/conda-forge/lagranto-feedstock.
- Clone the fork locally.

PyPi
====

- A PyPi account
- A gpg key


General Steps
~~~~~~~~~~~~~

1. Change the version number in setup.py
2. Add a tag for this new version:

.. code-block:: bash

    git tag -s TAGNAME -u KEY

3. Push the tag:

.. code-block:: bash

    git push --tags

PyPi
~~~~

Simply run:

.. code-block:: bash

    ./pypi_upload.sh


Conda
~~~~~

Edit the version name and the sha256 sum of Lagranto in recipe/meta.yaml.
The sha256 can be determined as follow:

.. code-block:: bash

    wget "https://git.iac.ethz.ch/atmosdyn/Lagranto/repository/VERSION/archive.tar.gz"
    sha245sum archive.tar.gz

Commit and push the changes, and on github create a pull-request on conda-forge/lagranto-feedstock



.. |docs| image:: https://readthedocs.org/projects/lagranto/badge/?version=latest
    :target: http://lagranto.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status


.. |pipelines| image:: https://gitlab.com/atmosdyn/Lagranto/badges/master/pipeline.svg
    :target: https://gitlab.com/atmosdyn/Lagranto/commits/master
