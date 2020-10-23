import os
from time import sleep

from decouple import config
from google.oauth2 import service_account
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

API_KEY = config('API_KEY')

YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
CLIENT_SECRETS_FILE = "client_secrets.json"
MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

   %s

with information from the API Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""" % os.path.abspath(os.path.join(os.path.dirname(__file__),
                                   CLIENT_SECRETS_FILE))

YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'


def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        'client_secret.json',
        scopes=[YOUTUBE_READ_WRITE_SCOPE])

    credentials = flow.run_local_server()

    return build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, credentials=credentials)


youtube = get_authenticated_service()

youtube


class VideoAlreadyUpdated(Exception):
    pass


def video_description_replace(video_id, current_description):
    final_cta_link = 'http://bit.ly/curso-de-programacao-intermediario'
    cta_text = cta_text_template.format(video_id=video_id)
    new_description_link = 'https://www.python.pro.br/curso-de-django?utm_source=youtube&utm_medium=trafego-organico&utm_campaign=video'
    if new_description_link in current_description:
        raise VideoAlreadyUpdated()

    if final_cta_link in current_description:
        video_description = current_description.split(final_cta_link)[-1].strip()
    elif '---' in current_description:
        video_description = current_description.split('---')[1].strip()
    else:
        video_description = current_description.strip()

    new_description = description_template.format(video_description=video_description, cta_text=cta_text)
    return new_description


def list_youtube_video_ids() -> set:
    video_set = set()
    pageToken = None
    while True:
        js = youtube.search().list(
            part="id",
            channelId='UCGjx62365UJ8XTWU_5GZC-g',
            pageToken=pageToken,
            maxResults=50
        ).execute()
        items = js['items']
        if len(items) == 0:
            break
        pageToken = js['nextPageToken']
        for item in items:
            id_data = item['id']
            if id_data['kind'] == 'youtube#video':
                video_set.add(id_data['videoId'])
        sleep(1)

    return video_set


def edit_video_description(video_id):
    # Obter Descrição
    js = youtube.videos().list(part="id,snippet", id=video_id).execute()
    snippet = js['items'][0]['snippet']
    video_current_description = snippet['description']
    try:
        new_description = video_description_replace(video_id, video_current_description)
    except VideoAlreadyUpdated:
        print(f'Video já alterado {video_id}')
    else:
        snippet['description'] = new_description
        youtube.videos().update(
            part='snippet',
            body=dict(
                snippet=snippet,
                id=video_id
            )
        ).execute()


def edit_all_channel_video_descriptions(video_ids_set: set):
    while len(video_ids_set) > 0:
        video_id = video_ids_set.pop()
        print(f'#####################  Editando video {video_id}')
        edit_video_description(video_id)
        sleep(1)
        print(f'Faltando videos: {video_ids_set!r}')


cta_text_template = """💡 Quer aprender Django? Eu preparei um curso especial pra você! Matricule-se no link:
https://www.python.pro.br/curso-de-django?utm_source=youtube&utm_medium=trafego-organico&utm_campaign=video-{video_id}

🔴 Quer conhecer o caminho mais rápido para você conquistar sua primeira oportunidade como programador e iniciar uma carreira à prova de crise? Clique no link: https://www.python.pro.br/r/landing-page-rumo-a-primeira-vaga?utm_source=youtube&utm_medium=trafego-organico&utm_campaign=video-{video_id}

🗣 Grupo de discussão dos conteúdos Python Pro: https://bit.ly/galera-python-pro
🗣 Fique por dentro de todas nossas novidades: https://bit.ly/canal-python-pro
"""

description_template = """{cta_text}
---

{video_description}

---

🎧 Ouça o Podcast DevPro: https://t.ly/XGM2w

👤 Siga-nos nas Redes sociais:
👉🏻 Instagram: https://instagram.com/renzoprobr
👉🏻 Twitter: https://twitter.com/renzoprobr
👉🏻 Facebook: https://www.facebook.com/pythonprobr
👉🏻 Linkedin: https://www.linkedin.com/in/renzonuccitelli/

🐍 Conheça o Python Pro!
👉🏻 Python Pro: http://python.pro.br"""

if __name__ == '__main__':
    video_ids_set = list_youtube_video_ids()
    edit_all_channel_video_descriptions(video_ids_set)

    # Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
    # tab of
    #   https://cloud.google.com/console
    # Please ensure that you have enabled the YouTube Data API for your project.
