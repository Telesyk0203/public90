import requests
from .models import TeleSettings

def sendTelegram(tg_name, tg_phone):
    settings= TeleSettings.objects.get(pk=2)
    token = str(settings.tg_token)
    chat_id = str(settings.tg_chat_id)
    text = str(settings.tg_text)
    time=str(settings.tg_time)
    api= 'https://api.telegram.org/bot'
    method= api + token + '/sendMessage'
    
    
    a=text.find('{')
    b= text.find('}')
    c= text.rfind('{')
    d=text.rfind('}')

    part_1= text[0:a]
    part_2= text[b+1:c]
    part_3= text[d:-1]

    text_slise= part_1 +tg_name +  part_2 + tg_phone + part_3
    
    req= requests.post(method, data={
        'chat_id':chat_id,
        'token':token,
        'text':text_slise,
        'time': time
    })

