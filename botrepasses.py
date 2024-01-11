from telethon import TelegramClient, sync
from time import sleep
import requests
from senhas import api_hash, api_id

sessao = 'Repassar mensagems'

def obter_chats():
    
    client = TelegramClient(sessao, api_id, api_hash)
    client.start()
    dialogs = client.get_dialogs()
    for dialog in dialogs:
        print('-----------------------')
        if dialog.id < 0:
            print(f'Grupo: {dialog.title}')
            print(f'id: {dialog.id}')
        else:
            print(f'Grupo: {dialog.title}')
            print(f'id: {dialog.id}')
        print('-----------------------\n')
    client.disconnect()

def main():
    print('Coletando dados de Adaylson Melo...\n')
    print('Monitoramento iniciado.')
    client = TelegramClient(sessao, api_id, api_hash)
    print(client)
    #0client.on(events.NewMessage(chats = [1001597109482]))
    #async def enviar_mensagem(event):
     #  await client.send_messagem(1002123958418,event.raw_text)
    #client.start()
    #client.run_untill_disconnected()
            

