import datetime

def tabla():

    grid = SQLFORM.grid(db.Signals, csv=False)

    return dict(hora=datetime.datetime.now() , grid=grid)

def registro():
   formulario = SQLFORM(db.Signals)
   if formulario.process().accepted:
       response.flash = 'formulario aceptado'
   elif formulario.errors:
       response.flash = 'el formulario tiene errores'
   else:
       response.flash = 'por favor complete el formulario'
   return dict(formulario=formulario)

def termometro():
    return dict()


def valor_potenciometro():
    potenciometro = db(db.Signals.nombre=='Potenciómetro').select().first()
    potenciometro_id = potenciometro.id

    registro_potenciometro = db(db.Valores.direccion==potenciometro_id).select().last()

    return dict(potenciometro=registro_potenciometro.valor)


def prueba():
    # como la página de la graica con plotly o chartist
    # solo cambia en la parte de JavaScript, hago una
    # función para las dos, ya que en Python son idénticas

    # obtener el id de la señal llamada Potenciómetro:
    potenciometro = db(db.Signals.nombre=='Potenciómetro').select().first()
    potenciometro_id = potenciometro.id
    
    # obtener un grid con los valores sólo del potenciómetro:
    grid = SQLFORM.grid(db.Valores.direccion==potenciometro_id, csv=False,
    fields=(db.Valores.Fecha, db.Valores.valor),
    searchable=False, details=False)

    return dict(rejilla=grid)

def grafica_chartist():
    return prueba()

def grafica_plotly():
    return prueba()

def datos_potenciometro():
    potenciometro = db(db.Signals.nombre=='Potenciómetro').select().first()
    potenciometro_id = potenciometro.id

    condicion = db.Valores.direccion==potenciometro_id and db.Valores.Fecha < '2020-11-05 10:24'

    datos = db(condicion).select(db.Valores.Fecha, db.Valores.valor)

    return dict(datos=datos)