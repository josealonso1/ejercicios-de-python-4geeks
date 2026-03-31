# Desafios de Codigo para Entrevistas en 4Geeks Academy

<!-- hide -->
> Por [@ehiber](https://github.com/ehiber), [@marcogonzalo](https://github.com/marcogonzalo), [@alesanchezr](https://github.com/alesanchezr), [@Charlytoc](https://github.com/Charlytoc) y contribuidores de [4Geeks Academy](https://4geeksacademy.com/)

[![build by developers](https://img.shields.io/badge/build_by-Developers-blue)](https://4geeks.com)
[![twitter](https://img.shields.io/twitter/follow/4geeksacademy?style=social&logo=twitter)](https://twitter.com/4geeksacademy)

*These instructions are available in [english](./README.md).*
<!-- endhide -->

Practica desafios de codigo tipo entrevista con ejercicios progresivos y autoevaluacion aislada en Python.

## Instalacion en un clic (recomendado)

Abre en [Codespaces](https://codespaces.new/) y ejecuta:

```bash
learnpack start
```

## Instalacion local

1. Instala LearnPack y el plugin de Python:
```bash
npm i @learnpack/learnpack -g
learnpack plugins:install @learnpack/python@1.0.0
```
2. Instala las dependencias de pruebas:
```bash
python3 -m pip install -r requirements.txt
```
3. En la carpeta donde existe este `learn.json`, ejecuta:
```bash
learnpack start
```

## Estructura de ejercicios

El repositorio incluye:

1. `exercises/00-welcome`: Paso introductorio solo con readme.
2. `exercises/01-...` hasta `exercises/15-...`: Retos de codigo.

La mayoria de carpetas de ejercicios incluye:

1. `app.py`: Archivo inicial para estudiantes.
2. `README.md`: Instrucciones en ingles.
3. `README.es.md`: Instrucciones en espanol.
4. `test.py`: Entrada de tests del ejercicio.
5. `solution.hide.py` (en algunos ejercicios): Solucion de referencia oculta.

## Notas

- Mantener `README.md` y `README.es.md` sincronizados cuando se cambie contenido.
- Los archivos `app.py` estan intencionalmente sin resolver para estudiantes.
