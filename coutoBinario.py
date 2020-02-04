#importar módulo tweepy
import tweepy
import time
from funcoes import *
from threading import Thread

def coutoBinario():
    '''
    Aonde a lógica central vive. 
    '''
    #Twitter developer API tokens
    consumer_key = "xxxxxx"
    consumer_secret = "xxxxxxx"
    access_token = "xxxxxxxxxx"
    access_token_secret = "xxxxxxx"  

    #autenticar
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #cria objeto API e pede pra que o aquivo venha como JSON
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    #conta a ser analisada
    acc = "ContaDoTuíter" 

    #taxa de verificação em segundos
    sec = 60
    
    antigos = puxaUltimos20(api, acc)

    while True:
        #puxa lista dos últimos 20 novos tuítes
        novos = puxaUltimos20(api, acc)

        #compara as listas de tuítes antigos e novos
        if antigos != novos:

            #guarda os tuítes diferentes
            diferenca = [x for x in novos if x not in antigos]

            #para cada tuíte que ainda nao foi respondido
            for tuite in diferenca:
                #converte o texto
                convertido = toBin(acc, tuite[1])
                #tuíta a lista de resposta
                tuitaRespostaLista(convertido, tuite[0], api)
                #atualiza tuítes antigos
                antigos = novos

            #aguarda "sec" segundos
            time.sleep(sec)
            
        else:
            print("Nenhum tuíte novo esperar!")
            #aguarda "sec" segundos
            time.sleep(sec)

def coutoNervoso():
    '''
    Aonde a lógica central vive. 
    '''
    #Twitter developer API tokens
    consumer_key = "XXXXXXX"
    consumer_secret = "XXXXXXXX"
    access_token = "XXXXXXXX"
    access_token_secret = "XXXXXXXX"  

    #autenticar
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    #cria objeto API e pede pra que o aquivo venha como JSON
    api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())

    #conta a ser analisada
    acc = "ContaDoTuíter" 

    #taxa de verificação em segundos
    sec = 60
    
    antigos = puxaUltimos20(api, acc)

    while True:
        #puxa lista dos últimos 20 novos tuítes
        novos = puxaUltimos20(api, acc)

        #compara as listas de tuítes antigos e novos
        if antigos != novos:

            #guarda os tuítes diferentes
            diferenca = [x for x in novos if x not in antigos]

            #para cada tuíte que ainda nao foi respondido
            for tuite in diferenca:
                #converte o texto
                convertido = toNervoso(acc, tuite[1])
                #tuíta a lista de resposta
                tuitaRespostaLista(convertido, tuite[0], api)
                #atualiza tuítes antigos
                antigos = novos

            #aguarda "sec" segundos
            time.sleep(sec)
            
        else:
            print("Nenhum tuíte novo esperar!")
            #aguarda "sec" segundos
            time.sleep(sec)
        
if __name__ == "__main__":
    Thread(target = coutoBinario).start()
    Thread(target = coutoNervoso).start()
