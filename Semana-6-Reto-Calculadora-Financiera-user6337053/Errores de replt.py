Python 3.8.2 (default, Feb 26 2020, 02:56:10)

❌   test_simular_credito
Stack Trace:
Traceback (most recent call last):
  File "/home/runner/Semana-6-Reto-Calculadora-Financiera-user6337053/_test_runnertest_suite.py", line 13, in test_simular_credito
    self.assertEquals(simular_credito( 15000000, 0.175, 36, 529103.39, 22000, 0 ),
    [{'mes': 1, 'saldo_inicial': 15000000, 'intereses': 202945.83, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 14673842.44},
     {'mes': 2, 'saldo_inicial': 14673842.44, 'intereses': 198533.0, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 14343272.05},
     {'mes': 3, 'saldo_inicial': 14343272.05, 'intereses': 194060.48, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 14008229.14},
     {'mes': 4, 'saldo_inicial': 14008229.14, 'intereses': 189527.44, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 13668653.19},
     {'mes': 5, 'saldo_inicial': 13668653.19, 'intereses': 184933.07, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 13324482.87},
     {'mes': 6, 'saldo_inicial': 13324482.87, 'intereses': 180276.55, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 12975656.03},
     {'mes': 7, 'saldo_inicial': 12975656.03, 'intereses': 175557.02, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 12622109.66},
     {'mes': 8, 'saldo_inicial': 12622109.66, 'intereses': 170773.63, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 12263779.9},
     {'mes': 9, 'saldo_inicial': 12263779.9, 'intereses': 165925.53, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 11900602.04},
     {'mes': 10, 'saldo_inicial': 11900602.04, 'intereses': 161011.83, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 11532510.48},
     {'mes': 11, 'saldo_inicial': 11532510.48, 'intereses': 156031.66, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 11159438.75},
     {'mes': 12, 'saldo_inicial': 11159438.75, 'intereses': 150984.1, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 10781319.46},
     {'mes': 13, 'saldo_inicial': 10781319.46, 'intereses': 145868.25, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 10398084.32},
     {'mes': 14, 'saldo_inicial': 10398084.32, 'intereses': 140683.19, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 10009664.12},
     {'mes': 15, 'saldo_inicial': 10009664.12, 'intereses': 135427.97, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 9615988.7},
     {'mes': 16, 'saldo_inicial': 9615988.7, 'intereses': 130101.65, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 9216986.96},
     {'mes': 17, 'saldo_inicial': 9216986.96, 'intereses': 124703.27, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 8812586.84},
     {'mes': 18, 'saldo_inicial': 8812586.84, 'intereses': 119231.85, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 8402715.3},
     {'mes': 19, 'saldo_inicial': 8402715.3, 'intereses': 113686.4, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 7987298.31},
     {'mes': 20, 'saldo_inicial': 7987298.31, 'intereses': 108065.92, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 7566260.84},
     {'mes': 21, 'saldo_inicial': 7566260.84, 'intereses': 102369.4, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 7139526.85},
     {'mes': 22, 'saldo_inicial': 7139526.85, 'intereses': 96595.81, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 6707019.27},
     {'mes': 23, 'saldo_inicial': 6707019.27, 'intereses': 90744.1, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 6268659.98},
     {'mes': 24, 'saldo_inicial': 6268659.98, 'intereses': 84813.23, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 5824369.82},
     {'mes': 25, 'saldo_inicial': 5824369.82, 'intereses': 78802.1, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 5374068.53},
     {'mes': 26, 'saldo_inicial': 5374068.53, 'intereses': 72709.65, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 4917674.79},
     {'mes': 27, 'saldo_inicial': 4917674.79, 'intereses': 66534.77, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 4455106.17},
     {'mes': 28, 'saldo_inicial': 4455106.17, 'intereses': 60276.35, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 3986279.13},
     {'mes': 29, 'saldo_inicial': 3986279.13, 'intereses': 53933.25, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 3511108.99},
     {'mes': 30, 'saldo_inicial': 3511108.99, 'intereses': 47504.33, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 3029509.93},
     {'mes': 31, 'saldo_inicial': 3029509.93, 'intereses': 40988.43, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 2541394.97},
     {'mes': 32, 'saldo_inicial': 2541394.97, 'intereses': 34384.37, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 2046675.95},
     {'mes': 33, 'saldo_inicial': 2046675.95, 'intereses': 27690.96, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 1545263.52},
     {'mes': 34, 'saldo_inicial': 1545263.52, 'intereses': 20906.99, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 1037067.12},
     {'mes': 35, 'saldo_inicial': 1037067.12, 'intereses': 14031.23, 'total_cuota': 551103.39, 'abono_capital': 0, 'saldo_despues_pago': 521994.96},
     {'mes': 36, 'saldo_inicial': 521994.96, 'intereses': 7062.45, 'abono_capital': 0, 'total_cuota': 551057.41, 'saldo_despues_pago': 0.0}])
AssertionError: Lists differ: [{'me[27 chars]00000.0, 'intereses': 202945.83, 'total_cuota'[5155 chars]0.0}] !=
                              [{'me[27 chars]00000, 'intereses': 202945.83, 'total_cuota': [5153 chars]0.0}]

First differing element 35:
{'mes[53 chars]45, 'total_cuota': 551103.39, 'abono_capital':[25 chars] 0.0}
{'mes[53 chars]45, 'abono_capital': 0, 'total_cuota': 551057.[25 chars] 0.0}

Diff is 6220 characters long. Set self.maxDiff to None to see it.

Diff is 6302 characters long. Set self.maxDiff to None to see it.


selenium - web scraping (beautiful soup)- requests - cython - pyautogui . https://www.youtube.com/watch?v=iL2Qa_8Cmr8
