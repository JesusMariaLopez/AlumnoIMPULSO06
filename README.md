# AlumnoIMPULSO06
Repositorio IMPULSO 06

## Calculadora de consola en Python

Este proyecto incluye una calculadora aritmética básica que realiza:
- suma
- resta
- multiplicación
- división

### Uso

Ejecuta en la terminal:

```bash
python calculator.py
```

Luego elige la operación y proporciona los números solicitados.

## Interfaz gráfica en Python

También puedes usar una versión gráfica con Tkinter.

### Uso

Ejecuta en la terminal:

```bash
python calculator_gui.py
```

Se abrirá una ventana donde puedes ingresar los números, seleccionar la operación y ver el resultado.

## Interfaz web (Flask)

También hay una versión web que funciona en entornos sin servidor gráfico.

### Instalación

Instala dependencias:

```bash
pip install -r requirements.txt
```

### Ejecución

Ejecuta la aplicación:

```bash
python3 calculator_flask.py
```

Si el puerto `5000` está ocupado, puedes iniciar en otro puerto:

```bash
python3 calculator_flask.py --port 5001
```

o estableciendo la variable de entorno `PORT`:

```bash
PORT=5001 python3 calculator_flask.py
```

La app escuchará en http://0.0.0.0:<puerto>.

Si corres en un servidor que no expone puertos, puedes usar `xvfb-run` o acceder por túnel SSH con reenvío de puertos.
