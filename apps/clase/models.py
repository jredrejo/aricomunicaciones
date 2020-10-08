"""
This file defines the database models
"""

from .common import db, Field
from pydal.validators import *

### Define your table below
#
# db.define_table('thing', Field('name'))
#
## always commit your models to avoid problems later
#
# db.commit()
#

# para ver la documentación de como se definen los campos
# http://www.web2py.com/books/default/chapter/41/06/la-capa-de-abstraccion-de-la-base-de-datos#DAL-Table-Field

db.define_table('Autores',
    Field('Nombre',length=50),
    Field('Apellido', length=100, default="García"),
    Field('Nacimiento', 'date', required=True),
    format='%(Nombre)s %(Apellido)s'

)

db.define_table('Libros',
    Field('Titulo', label ="Título"),
    Field('Publicacion', 'datetime', label="Fecha de Publicación", required=True),
    Field('autor', db.Autores)

)
