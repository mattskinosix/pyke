

import pyke
import sys
import pyowm
from pyke import knowledge_engine
from pyke import krb_traceback
engine = knowledge_engine.engine(__file__)


def meteo(nome_citta):

    # viene utilizzata una API KEY gratuita

    owm = pyowm.OWM('ba25b6b66bf3f2ba2771dc6f80538142')  # You MUST provide a valid API key
    try:
        observation = owm.weather_at_place(nome_citta + ' ,IT')
        w = observation.get_weather()
        previsione = [w.get_status(), w.get_temperature('celsius'
                      )['temp']]
        return previsione
    except Exception:
        previsione = None
        return previsione

    
# from neo4j import GraphDatabase

def test(tempo, m):

    # uri = "bolt://192.168.1.15:7687"
    # driver = GraphDatabase.driver(uri, auth=("neo4j", "meocameo"))
    # print("dove vai?")

    #prev = meteo(input(': '))

    engine.reset()
    engine.activate('regole2')

    # engine.assert_('fatti', 'natura',('carino','forse'))
    # engine.assert_('fatti', 'tempo',('levante','')
   # if (prev[1]>28) :
    #        temp = 'calda'
   # elif 15<prev[1]<=28 :
     #       temp = 'mite'
   # elif 15>prev[1]:
    ##        temp='fredda'
    try:
        with engine.prove_goal('regole2.cosa_fare(Rain,mite,$risposta)') as \
            gen:
            for vars, plan in gen:
                print (('%s ' % vars['risposta']))
    except Exception:
        krb_traceback.print_exc()
        print("no")
   

test('bello', 'si')
