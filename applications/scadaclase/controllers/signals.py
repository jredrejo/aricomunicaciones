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
