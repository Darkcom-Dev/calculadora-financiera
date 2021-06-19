import matplotlib.pyplot as plt
import financial_controller as financial



def lanzar():
  """
    Inicializa la aplicación y llama en orden los métodos, para dar el flujo de la aplicación.
  """  
  iniciar_calculadora()
  capital, interes, plazo_meses, valor_seguro, abono_capital = solicitar_entradas()
  
  valor_cuota = financial.obtener_valor_cuota(capital, interes, plazo_meses)
  resultado_simulacion = financial.simular_credito( capital, interes, plazo_meses, valor_cuota, valor_seguro, abono_capital )

  mostrar_resultados( capital, valor_cuota, valor_seguro, resultado_simulacion, abono_capital )
  fin_calculadora()
  firma()

  graficar(resultado_simulacion)

def iniciar_calculadora():
  """
    Interfaz en consola de la calculadora financiera
  """
  print("""*****************************************************************************
***********************  CALCULADORA FINANCIERA  ****************************
*****************************************************************************
  """)
  

def fin_calculadora():
  """
    Interfaz en consola de la calculadora financiera
  """
  print("""
*****************************************************************************
*************************  CALCULO FINALIZADO  ******************************
*****************************************************************************""")


def mostrar_resultados(capital_inicial, valor_cuota, seguro, simulacion, abono_capital):
  print()
  print("Mes {}: Desembolso: {}".format(0, capital_inicial) )
  print("Valor de la cuota: {}".format(valor_cuota) )

  header = '|     Mes     |     Capital Base     |     Intereses     |     Seguro     |     Total Cuota     |     Abono a capital     |     Saldo después del pago     |'
  print( header )

  count = 0
  for data in simulacion:
    count += 1
    linea = '|'
    
    columan = ' {} '.format( data['mes'] )
    while len(columan) < 13:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['saldo_inicial'] )
    while len(columan) < 22:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['intereses'] )
    while len(columan) < 19:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( seguro )
    while len(columan) < 16:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['total_cuota'] )
    while len(columan) < 21:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['abono_capital'] )
    while len(columan) < 25:
      columan = ' ' + columan
    linea += columan + '|'

    columan = ' {} '.format( data['saldo_despues_pago'] )
    while len(columan) < 32:
      columan = ' ' + columan
    linea += columan + '|'

    print( linea )

  



def firma():
  """
    Muestra el nombre del creador de la aplicacion
  """
  firma = {
    'nombre': 'Braulio León Madrid Escobar', # Colocar su nombre completo
  }
  print("Este desarrollo fue creado por: {}".format(firma['nombre']))
  return firma['nombre']
  


def solicitar_entradas() -> tuple:
  '''
  Toma los datos necesarios por parte del cliente para efectuar la simulación:

  Retorna:
  ----
  tuple = (capital:float, interese:float, plazo_meses:int, valor_seguro:int, abono_capital:int)
  '''
  
  capital: float # es la cantidad base del prestamo
  intereses: float # es el porcentaje de interes aplicado al capital
  plazo_meses: int # tiempo al que se debita el prestamo
  valor_seguro: int # valor del seguro de impago crediticio
  abono_capital: float # abono al capital base del prestamo
  
  # TODO: Desarrollar este código
  
  try:
    capital = float(input('Por favor ingrese el monto solicitado: '))
    intereses = float(input('Por favor ingrese el interes efectivo anual, dado por la entidad financiera: '))
    plazo_meses = int(input('Por favor ingrese el número de meses: '))
    valor_seguro = int(input('Por favor ingrese el valor del seguro: '))
    abono_capital = int(input('Por favor ingrese el esperado abono al capital: '))
  except:
    capital = float(15000000)
    intereses = float(17.5/100)
    plazo_meses = 60
    valor_seguro = 22000
    abono_capital = 250000

  return capital, intereses/100, plazo_meses, valor_seguro, abono_capital
  
def graficar (simulacion):
  
  mes = list()
  intereses = list()
  cuotas = list()

  for data in simulacion:
    mes.append(data['mes'])
    intereses.append(data['total_cuota']-data['intereses'])
    cuotas.append(data['total_cuota'])

  plt.bar(mes,cuotas, label = 'cuotas', color = 'blue')
  plt.bar(mes,intereses,label = 'intereses', color = 'orange')
  
  plt.title('Diagrama de linea')
  plt.xlabel('mes')
  plt.ylabel('intereses')
  plt.legend()
  plt.grid()
  plt.show()
  
