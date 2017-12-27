from urllib.request import Request, urlopen
import urllib.error
import time
import datetime

def retornaSomenteQuandoTiverSucesso(url, tempo=5):
    sucesso = False
    while sucesso is False:
        try:
            req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urlopen(req)

        except urllib.error.HTTPError as e:
            #Um erro 4xx ou 5xx
            print('HTTPErro: ', e.code)
            print("{0}/Erro vindo do link: {1}".format(datetime.datetime.now(), url))
            time.sleep(tempo)
            print("Tentando novamente")

        except urllib.error.URLError as e:
            #Um erro não relacionado com http
            print('URLPErro: ', e.reason)
            print("{0}/Erro vindo do link: {1}".format(datetime.datetime.now(), url))
            time.sleep(tempo)
            print("Tentando novamente")

        except Exception as e:
            #Um erro qualquer
            print('Erro', e)
            print("{0}/Erro vindo do link: {1}".format(datetime.datetime.now(), url))
            time.sleep(tempo)
            print("Tentando novamente")

        else:
            #Retorno 200
            return response.read().decode('utf-8')