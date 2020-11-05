def inicio():
    led = db(db.Signals.nombre=='Led').select().first()
    led_id = led.id

    orden_led = db(db.Ordenes.direccion==led_id).select().first()



    return dict(estado=orden_led.valor)

def recibirorden():
    led = db(db.Signals.nombre=='Led').select().first()
    led_id = led.id
    orden_led = db(db.Ordenes.direccion==led_id).select().first()

    if request.vars.encender == '1':
        print(" es un niño")
        orden_led.update_record(valor=1.0)
    else:
        print(" es una niña")
        orden_led.update_record(valor=0.0)
    
    db.commit()

    return dict(mensaje="hola")