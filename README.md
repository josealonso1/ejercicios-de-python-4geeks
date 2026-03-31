# Interview Coding Challenges at 4Geeks Academy

<!-- hide -->
> By [@ehiber](https://github.com/ehiber), [@marcogonzalo](https://github.com/marcogonzalo), [@alesanchezr](https://github.com/alesanchezr), [@Charlytoc](https://github.com/Charlytoc) and contributors at [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![twitter](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=twitter)](https://twitter.com/4geeksacademy)

*Estas instrucciones estan disponibles en [espanol](./README.es.md).*
<!-- endhide -->

Practice interview-style coding challenges with progressive exercises and isolated auto-evaluation in Python.

## One-click setup (recommended)

Open in [Codespaces](https://codespaces.new/) and run:

```bash
learnpack start
```

## Local setup

1. Install LearnPack and the Python plugin:
```bash
npm i @learnpack/learnpack -g
learnpack plugins:install @learnpack/python@1.0.0
```
2. Install Python test dependencies:
```bash
python3 -m pip install -r requirements.txt
```
3. From the folder where this `learn.json` exists, then run:
```bash
learnpack start
```

## Exercise structure

The repository includes:

1. `exercises/00-welcome`: Introductory readme-only step.
2. `exercises/01-...` to `exercises/15-...`: Coding challenges.

Most exercise folders include:

1. `app.py`: Starter file for students.
2. `README.md`: Instructions in English.
3. `README.es.md`: Instructions in Spanish.
4. `test.py`: Exercise test entry.
5. `solution.hide.py` (on selected exercises): Hidden reference solution.

## Notes

- Keep `README.md` and `README.es.md` synchronized when content changes.
- Student files are intentionally unsolved in `app.py`.
