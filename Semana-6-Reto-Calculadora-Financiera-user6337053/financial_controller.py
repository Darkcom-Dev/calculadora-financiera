def simular_credito( capital, interes, plazo_meses, valor_cuota, valor_seguro, abono_capital ) -> dict:
  '''
  Devuelve una lista desglosada de saldos, intereses, cuotas, abonos

  Parametros:
  ----
  capital : float
  interes : float
  plazo_meses : int
  valor_cuota : int
  valor_seguro : int
  abono_capital : int

  Retorna:
  fila : dict
    mes: int
    saldo_inicial: float
    total_cuota: float
    abono_capital: int
    saldo_despues_pago: float
  '''
  
  result = list()
  saldo_ini = float(capital)
  for m in range(1,plazo_meses+1):

    ints = saldo_ini * convertir_interes_efectivo_anula_a_mensual(interes)
       
    saldo_a_pagar = saldo_ini + ints + valor_seguro

    t_cuota = float()
    if saldo_a_pagar > valor_cuota + valor_seguro:
      t_cuota = valor_cuota + valor_seguro # V
    else:
      t_cuota = saldo_a_pagar
      
    
    abono = control_abonos(saldo_a_pagar,t_cuota,abono_capital)

    # si las deducciones llegan a ser cero o negativas, el saldo final debe ser 0
    if saldo_a_pagar - t_cuota - abono <= 0:
      saldo_fin = 0.0
    # sino muestre el saldo final tal cual es
    else:
      saldo_fin = saldo_a_pagar - t_cuota - abono # V

    fila = {'mes':m,
            'saldo_inicial':round(saldo_ini,2),
            'intereses':round(ints,2),
            'total_cuota':round(t_cuota,2),
            'abono_capital':round(abono,2),
            'saldo_despues_pago':round(saldo_fin,2)}
    result.append(fila)
    if saldo_fin > 0:
      saldo_ini = round(saldo_fin,2)
    else:
      break
    
  return result

def control_abonos(saldo_a_pagar, cuota_mensual, abono_capital_esperado):
  '''
  Retorna los abonos calculados
  '''
  # Si el abono_capital es 0 o menor, el abono es 
  if abono_capital_esperado <= 0:
    return 0
  # si el abono es mayor a cero y aun las deducciones son mayores al capital
  elif saldo_a_pagar - cuota_mensual > abono_capital_esperado and abono_capital_esperado > 0:
    return abono_capital_esperado # V
  # si no, el abono al capital será el restante a la deduccion
  else:
    return saldo_a_pagar - cuota_mensual


def calcular_nuevo_valor_adeudado( capital, interes ) -> float:
  # TODO: Documentar Método
  # TODO: Desarrollar este método
  # AYUDA: usar el método "convertir_interes_efectivo_anula_a_mensual" para convertir el interes de anual a mensual

  
  capFinal = capital * (1 + convertir_interes_efectivo_anula_a_mensual(interes))
  
  return round(capFinal,2)


def convertir_interes_efectivo_anula_a_mensual(ea):
  """
    Convierte el interes de efectivo anula a efectivo mensual
  """  
  return (1 + ea)**(1/12) - 1

def obtener_valor_cuota(monto, tasa, cuotas):
    """
    Retorna el valor actual de la cuota, para cuotas son fijas.
                
    Formula = R = P [(i (1 + i)**n) / ((1 + i)**n – 1)]. 
    Donde: 
        R = renta (cuota)
        P = principal (préstamo adquirido)
        i = tasa de interés
    """
    i = convertir_interes_efectivo_anula_a_mensual(tasa)
    c = (1 + i)**cuotas
    a = i * c
    b = c - 1
    valor_cuota = monto * (a / b)
    valor_cuota = valor_cuota + 1 # método para evitar un més adicional (truco)
    return round( valor_cuota, 2)


