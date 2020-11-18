# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

# ----------------------------------------------------------------------------------------------------------------------
# this is the main application menu add/remove items as required
# ----------------------------------------------------------------------------------------------------------------------

response.menu = [
    ('Potenciómetro', False, '#', [
        ('Datos', False, URL('default', 'potenciometro'), []),
        ('Gráfica con chartist', False, URL('signals', 'grafica_chartist'), []),
        ('Gráfica con plotly', False, URL('signals', 'grafica_plotly'), [])

    ]),
    ('Led', False, URL('pantalla', 'inicio'), []),
    ('Termómetro', False, URL('signals', 'termometro'), []),
    ('Señales', False, '#', [
        ('Nueva', False, URL('signals', 'registro'), []),
        ('Datos', False, URL('signals', 'tabla'), []),
    ]),
]
