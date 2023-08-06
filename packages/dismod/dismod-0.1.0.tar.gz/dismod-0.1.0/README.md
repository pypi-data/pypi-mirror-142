[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/r0x0d/dismod/main.svg)](https://results.pre-commit.ci/latest/github/r0x0d/dismod/main)
[![Coverage](https://github.com/r0x0d/dismod/actions/workflows/coverage.yml/badge.svg)](https://github.com/r0x0d/dismod/actions/workflows/coverage.yml)
[![codecov](https://codecov.io/gh/r0x0d/dismod/branch/main/graph/badge.svg?token=LSVRFFXPV5)](https://codecov.io/gh/r0x0d/dismod)
[![Total alerts](https://img.shields.io/lgtm/alerts/g/r0x0d/dismod.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/r0x0d/dismod/alerts/)
[![Language grade: Python](https://img.shields.io/lgtm/grade/python/g/r0x0d/dismod.svg?logo=lgtm&logoWidth=18)](https://lgtm.com/projects/g/r0x0d/dismod/context:python)
[![Code Scanning - Action](https://github.com/r0x0d/dismod/actions/workflows/codeql.yml/badge.svg)](https://github.com/r0x0d/dismod/actions/workflows/codeql.yml)

# dismod

This tool aims to generate a dependency graph of the imports in your python
modules. It automatically search for every file with an extesion of `.py` and
quickly generate renderings of that file with all imports (used and unused).

# Usage

To use `dismod`, first you need to install it using `pip`

```bash
pip install dismod
```

After installed (can be insid a virtualenv or not), go to the project you want
to generate the graphs and run:

```bash
dismod <path_of_project>
```

For example, let's use `dismod` own repository to generate some graphs:

```bash
git clone git@github.com:r0x0d/dismod
cd dismod
dismod dismod
ls renders
```
