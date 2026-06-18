#!/usr/bin/env python3
from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev'

    @app.route('/', methods=['GET', 'POST'])
    def index():
        result = None
        error = None
        a = ''
        b = ''
        op = 'sum'

        if request.method == 'POST':
            a = request.form.get('a', '').strip()
            b = request.form.get('b', '').strip()
            op = request.form.get('op', 'sum')
            try:
                a_val = float(a)
                b_val = float(b)
                if op == 'sum':
                    result = a_val + b_val
                elif op == 'sub':
                    result = a_val - b_val
                elif op == 'mul':
                    result = a_val * b_val
                elif op == 'div':
                    if b_val == 0:
                        error = 'No se puede dividir por cero.'
                    else:
                        result = a_val / b_val
                else:
                    error = 'Operación inválida.'
            except ValueError:
                error = 'Entrada inválida. Ingresa números.'
            except Exception as exc:
                error = f'Error al calcular: {exc}'

        return render_template('index.html', result=result, error=error, a=a, b=b, op=op)

    return app


if __name__ == '__main__':
    import argparse
    import os
    import errno

    parser = argparse.ArgumentParser(description='Calculadora Flask')
    parser.add_argument('--port', type=int, default=int(os.environ.get('PORT', 5000)), help='Puerto para el servidor')
    args = parser.parse_args()

    app = create_app()
    port = args.port
    while True:
        try:
            app.run(host='0.0.0.0', port=port, debug=True)
            break
        except OSError as exc:
            if hasattr(exc, 'errno') and exc.errno == errno.EADDRINUSE:
                print(f'Puerto {port} en uso. Probando puerto {port + 1}...')
                port += 1
                continue
            raise
