# Calculadora en Python

Este proyecto fue desarrollado como parte de la Actividad 3 de la asignatura **Procesos en Ingeniería del Software** (PIS), con el objetivo de reforzar conceptos de programación y pruebas unitarias.

## Funcionalidad

La calculadora implementa 4 operaciones básicas:

- Suma
- Resta
- Multiplicación
- División (con control de error por división entre cero)

## Pruebas unitarias

Las pruebas se desarrollaron con `unittest` y cubren:

- Casos normales (positivos, negativos, cero)
- Errores comunes (`ZeroDivisionError`, `TypeError`)
- Casos extremos (`NaN`, `Infinity`)
- Validación de precisión decimal

## Como ejecutar

Desde la carpeta del proyecto, ejecutar:

python -m unittest test_calculadora.py

## Automatización con GitHub Actions

Este repositorio incluye un sistema de integración continua configurado con GitHub Actions.
Cada vez que se sube código, se ejecutan automaticamente todas las pruebas para garantizar que las operaciones matematicas siguen funcionando correctamente.
El estado y el historial de las ejecuciones pueden verse en la pestaña de Actiones del repositorio.