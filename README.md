# Práctica SSII - Grupo XX

## Autores

Álvaro Cabo - 200172

Samuel Salgueiro - 200245

## Set-up

Para esta practica hacemos uso de la implementación del estandar **FIPA** en Python: ["PADE"](https://pade.readthedocs.io/en/latest/)

### Requirements

- Python 3.X, se recomienda crear un [entorno virtual](https://docs.python.org/3/library/venv.html) para este proyecto:

  ```bash
  python -m venv venv # Creación del entorno
  source venv/bin/activate # Activación
  ```

- Gestor de paquetes, recomendamos [pip](https://pypi.org/project/pip/)
- Pade

  ```bash
  pip install pade
  ```

## Start-up

Para inciar el programa:

```bash
pade start-runtime --port 20000 agent_example_1.py
```
