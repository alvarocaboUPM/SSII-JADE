# RealTime data fetcher con Sistemas Autónomos

Práctica de la asignatura SSII del grupo XX

## Autores

| Nombre           | Matricula |
| ---------------- | --------- |
| Álvaro Cabo      | 200172    |
| Samuel Salgueiro | 200245    |

## Set-up

Para esta practica hacemos uso de la implementación del estandar **FIPA** en Python: ["PADE"](https://pade.readthedocs.io/en/latest/)

### Pre-requirements

Esta configuración se ha probado en Ubuntu 22.04 con Python 3.10.12

- Un gestor de paquetes de Python, nosotros
  usaremos [Pip](https://pypi.org/project/pip/)

- Python 3.10+, se recomienda crear u [entorno virtual](https://docs.python.org/3/library/venv.html) para este proyecto:

  ```bash
  pip install virtualenv # Instalamos virtualenv
  virtualenv .venv # Creación del entorno
  source .venv/bin/activate # Activación
  pip install -r requirements.txt # Instalación de requirements
  ```

- Pade, instalación manual

  ```bash
  mkdir lib && cd lib # Carpeta para guardar el código fuente
  git clone https://github.com/alvarocaboUPM/pade && cd pade && python setup.py install # Instalador de dependencias
  cd ../../ && rm -rf lib  # Opcional, borrar la carpeta lib pues ya no es necesaria
                           # puede generar conflicto con las dependencias ya instaladas en el entorno
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
pade start-runtime --port 20000 --username test --password test src/pub_sub_agent.py
```
