Changelog
=========

v0.3.1 (16.03.2022)
-------------------

- Fix version (was left at 0.2.0).


v0.3.0 (16.03.2022)
-------------------

- Drop support of python 2.7 and 3.6. lagranto is now python 3.7+.
- Fix deprecation of `np.float`, update a test figure, un-xfail tests relying on path.py.
- Reformatted with isort, black and flake8.


v0.2.0 (25.10.2019)
-------------------

- Extend functionality such that files with varying start time can be read (mathause).
- Open normal and gzipped files the same way: this allowed to remove duplicate
  code (mathause).
- The upstream ``path.py`` library has a problem (https://github.com/jaraco/path.py/issues/171)
  -> ``lagrantorun`` is currently not working (mathause).
- Reformatted with black. Checked with flake8 (mathause).
