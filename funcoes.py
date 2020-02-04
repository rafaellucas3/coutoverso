def tuitaRespostaLista(piuList, tuiteID, api):
    '''
    Tuíta uma lista de tuítes em resposta a um outro tuíte.
    Argumentos: 
        api (object): O objeto api do tweepy
        piuList (string list) = Lista de textos a serem tuitados
        tuiteID (string) = ID do tuíte a ser respondido
    '''
    for piu in piuList: 
        api.update_status(piu, in_reply_to_status_id=tuiteID) 

def toBin(acc, texto):
    '''
    Converte um texto em binario e retorna uma lista de strings 
    já com o tamanho certo e pronta para ser tuítado como resposta.

    Argumentos: 
        acc (string): conta a ser respondida
        texto (string): tuíte original
    
    Retorno:
        list: retorna lista com os tuítes convertidos
    '''
    #converte texto em binario
    binario = " ".join(f"{ord(i):08b}" for i in texto)

    #constrói resposta
    reply = "@"+acc+" "+binario

    #cria os novos tweets e coloca em uma lista (cortando a resposta para caber)
    size = 280
    tweets = [reply[i: i + size] for i in range(0, len(reply), size)]

    return tweets

def toNervoso(acc, texto):
    '''
    Converte um texto em nervoso e retorna uma lista de strings 
    já com o tamanho certo e pronta para ser tuítado como resposta.

    Argumentos: 
        acc (string): conta a ser respondida
        texto (string): tuíte original
    
    Retorno:
        list: retorna lista com os tuítes convertidos
    '''
    #converte texto em binario
    maiusculo = "POW... "+ texto.upper() + " CARAI!!"

    #constrói resposta
    reply = "@"+acc+" "+ maiusculo

    #cria os novos tweets e coloca em uma lista (cortando a resposta para caber)
    size = 280
    tweets = [reply[i: i + size] for i in range(0, len(reply), size)]

    return tweets

def puxaUltimos20(api, acc):
    '''
    Retorna uma lista com os 20 últimos tuítes da conta fornecida.

    Argumentos:
        api (object): O objeto api do tweepy
        acc (string): conta do tuíter a ser consultada

    Retorno:
        list: lista com os últimos 20 tuítes da conta fornecida
    ''' 
    #puxa o último tweet
    tweets = api.user_timeline(acc)

    listaTuites = []
    for tweet in tweets:
        #grava o id do tweet
        tweetID = tweet["id"]

        #seleciona só o texto do tweet
        texto = tweet["text"]

        #adiciona o id e texto na lista
        listaTuites.append([tweetID, texto])
    return listaTuites