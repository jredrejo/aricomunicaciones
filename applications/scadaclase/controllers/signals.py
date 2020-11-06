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