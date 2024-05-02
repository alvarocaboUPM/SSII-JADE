# Práctica SSII - Grupo XX

## Set-up

Para esta practica hacemos uso de la implementación del estandar **FIPA** en Python: ["PADE"](https://pade.readthedocs.io/en/latest/)

### Pre-requirements

- Un gestor de paquetes de Python, nosotros
  usaremos [Pip](https://pypi.org/project/pip/)

- Python 3.10+, se recomienda crear u [entorno virtual](https://docs.python.org/3/library/venv.html) para este proyecto:

  ```bash
  pip install virtualenv # Instalamos virtualenv
  virtualenv .venv # Creación del entorno
  source .venv/bin/activate # Activación
  ```

- Pade, instalación manual

  ```bash
  mkdir lib && cd lib # Carpeta para guardar el código fuente
  git clone https://github.com/alvarocaboUPM/pade && cd pade && python setup.py install # Instalador de dependencias
  ```

  Para comprobar que se ha instalado correctamente:

  ```bash
  pade
  ```

  Y obtendremos

  ```txt
  ❯ pade
  Usage: pade [OPTIONS] COMMAND [ARGS]...

  Options:
  --help  Show this message and exit.

  Commands:
  create-pade-db
  drop-pade-db
  start-runtime
  start-web-interface
  ```

## Start-up

Para inciar el programa:

```bash
cd SSII-JADE # Carpeta root del proyecto
pade start-runtime --port 20000 agent_example_1.py
```

## Autores

| Nombre           | Matricula |
| ---------------- | --------- |
| Álvaro Cabo      | 200172    |
| Samuel Salgueiro | 200245    |
