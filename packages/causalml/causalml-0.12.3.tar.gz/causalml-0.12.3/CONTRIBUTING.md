# Contributing to CausalML

The **CausalML** project welcome community contributors.
To contribute to it, please follow guidelines here.

The codebase is hosted on Github at https://github.com/uber/causalml.

We use [`black`](https://black.readthedocs.io/en/stable/index.html) as a formatter to keep the coding style and format across all Python files consistent and compliant with [PEP8](https://www.python.org/dev/peps/pep-0008/). We recommend that you add `black` to your IDE as a formatter (see the [instruction](https://black.readthedocs.io/en/stable/integrations/editors.html)) or run `black` on the command line before submitting a PR as follows:
```bash
# move to the top directory of the causalml repository
$ cd causalml 
$ pip install -U black
$ black .
```

As a start, please check out outstanding [issues](https://github.com/uber/causalml/issues).
If you'd like to contribute to something else, open a new issue for discussion first.

## Development Workflow :computer:

1. Fork the `causalml` repo. This will create your own copy of the `causalml` repo. For more details about forks, please check [this guide](https://docs.github.com/en/github/collaborating-with-pull-requests/working-with-forks/about-forks) at GitHub.
2. Clone the forked repo locally
3. Create a branch for the change:
```bash
$ git checkout -b branch_name
```
4. Make a change
5. Test your change as described below in the Test section
6. Commit the change to your local branch
```bash
$ git add file1_changed file2_changed
$ git commit -m "Issue number: message to describe the change."
```
7. Push your local branch to remote
```bash
$ git push origin branch_name
```
8. Go to GitHub and create PR from your branch in your forked repo to the original `causalml` repo. An instruction to create a PR from a fork is available [here](https://docs.github.com/en/github/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork)

## Documentation :books:

[**CausalML** documentation](https://causalml.readthedocs.io/) is generated with [Sphinx](https://www.sphinx-doc.org/en/master/) and hosted on [Read the Docs](https://readthedocs.org/).

### Docstrings

All public classes and functions should have docstrings to specify their inputs, outputs, behaviors and/or examples. For docstring conventions in Python, please refer to [PEP257](https://www.python.org/dev/peps/pep-0257/).

**CausalML** supports the NumPy and Google style docstrings in addition to Python's original docstring with [`sphinx.ext.napoleon`](https://www.sphinx-doc.org/en/master/usage/extensions/napoleon.html). Google style docstrings are recommended for simplicity. You can find examples of Google style docstrings [here](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html)

### Generating Documentation Locally

You can generate documentation in HTML locally as follows:
```bash
$ cd docs/
$ pip install -r requirements.txt
$ make html
```

Documentation will be available in `docs/_build/html/index.html`.

## Test :wrench:

If you added a new inference method, add test code to the `tests/` folder.

### Prerequisites

**CausalML** uses `pytest` for tests. Install `pytest` and `pytest-cov`, and the package dependencies:
```bash
$ pip install pytest pytest-cov -r requirements.txt
```

### Building Cython

In order to run tests, you need to build the Cython modules
```bash
$ python setup.py build_ext --inplace
```

### Testing

Before submitting a PR, make sure the change to pass all tests and test coverage to be at least 70%.
```bash
$ pytest -vs tests/ --cov causalml/
```


## Submission :tada:

In your PR, please include:
- Changes made
- Links to related issues/PRs
- Tests
- Dependencies
- References

Please add the core Causal ML contributors as reviewers.
