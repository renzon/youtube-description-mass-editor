from main import video_description_replace


def test_right_description_replace():
    nova_descricao = video_description_replace(
        video_id='1234',
        current_description=descricao_antiga_certa
    )
    assert nova_descricao == nova_descricao_processada_da_antiga_certa


def test_wrong_description_replace():
    nova_descricao = video_description_replace(
        video_id='1234',
        current_description=descricao_antiga_errada
    )
    assert nova_descricao == nova_descricao_processada_da_antiga_errada


def test_no_link_on_description():
    nova_descricao = video_description_replace(
        video_id='1234',
        current_description=descricao_sem_link
    )
    assert nova_descricao == nova_descricao_sem_link

descricao_sem_link = """Nessa Tech Talk o Willian, aluno da Python Pro, mostrou pra gente como funciona um Aplicação de Página Única (Single Page Application) utilizando o framework Vue,js,"""
nova_descricao_sem_link = """💡 Quer aprender Django? Eu preparei um curso especial pra você! Matricule-se no link:
https://www.python.pro.br/curso-de-django?utm_source=youtube&utm_medium=trafego-organico&utm_campaign=video-1234

🔴 Quer conhecer o caminho mais rápido para você conquistar sua primeira oportunidade como programador e iniciar uma carreira à prova de crise? Clique no link: https://www.python.pro.br/r/landing-page-rumo-a-primeira-vaga?utm_source=youtube&utm_medium=trafego-organico&utm_campaign=video-1234

🗣 Grupo de discussão dos conteúdos Python Pro: https://bit.ly/galera-python-pro
🗣 Fique por dentro de todas nossas novidades: https://bit.ly/canal-python-pro

---

Nessa Tech Talk o Willian, aluno da Python Pro, mostrou pra gente como funciona um Aplicação de Página Única (Single Page Application) utilizando o framework Vue,js,

---

🎧 Ouça o Podcast DevPro: https://t.ly/XGM2w

👤 Siga-nos nas Redes sociais:
👉🏻 Instagram: https://instagram.com/renzoprobr
👉🏻 Twitter: https://twitter.com/renzoprobr
👉🏻 Facebook: https://www.facebook.com/pythonprobr
👉🏻 Linkedin: https://www.linkedin.com/in/renzonuccitelli/

🐍 Conheça o Python Pro!
👉🏻 Python Pro: http://python.pro.br"""
nova_descricao_processada_da_antiga_certa = """💡 Quer aprender Django? Eu preparei um curso especial pra você! Matricule-se no link:
https://www.python.pro.br/curso-de-django?utm_source=youtube&utm_medium=trafego-organico&utm_campaign=video-1234

🔴 Quer conhecer o caminho mais rápido para você conquistar sua primeira oportunidade como programador e iniciar uma carreira à prova de crise? Clique no link: https://www.python.pro.br/r/landing-page-rumo-a-primeira-vaga?utm_source=youtube&utm_medium=trafego-organico&utm_campaign=video-1234

🗣 Grupo de discussão dos conteúdos Python Pro: https://bit.ly/galera-python-pro
🗣 Fique por dentro de todas nossas novidades: https://bit.ly/canal-python-pro

---

Nesse episódio corrigimos um bug da maneira certa, para ter grande confiabilidade de que ele não vai voltar:

1) Identificamos o bug
2) Criamos teste que evidencia o bug
3) Consertamos
4) Homologamos

---

🎧 Ouça o Podcast DevPro: https://t.ly/XGM2w

👤 Siga-nos nas Redes sociais:
👉🏻 Instagram: https://instagram.com/renzoprobr
👉🏻 Twitter: https://twitter.com/renzoprobr
👉🏻 Facebook: https://www.facebook.com/pythonprobr
👉🏻 Linkedin: https://www.linkedin.com/in/renzonuccitelli/

🐍 Conheça o Python Pro!
👉🏻 Python Pro: http://python.pro.br"""

descricao_antiga_certa = """Quer aprender Python? Eu preparei um curso rápido e grátis pra você! Cadastre-se no link:
http://bit.ly/curso-basico-de-python-gratis

Curso para de programação intermediário:
http://bit.ly/curso-de-programacao-intermediario

Nesse episódio corrigimos um bug da maneira certa, para ter grande confiabilidade de que ele não vai voltar:

1) Identificamos o bug
2) Criamos teste que evidencia o bug
3) Consertamos
4) Homologamos"""

nova_descricao_processada_da_antiga_errada = """💡 Quer aprender Django? Eu preparei um curso especial pra você! Matricule-se no link:
https://www.python.pro.br/curso-de-django?utm_source=youtube&utm_medium=trafego-organico&utm_campaign=video-1234

🔴 Quer conhecer o caminho mais rápido para você conquistar sua primeira oportunidade como programador e iniciar uma carreira à prova de crise? Clique no link: https://www.python.pro.br/r/landing-page-rumo-a-primeira-vaga?utm_source=youtube&utm_medium=trafego-organico&utm_campaign=video-1234

🗣 Grupo de discussão dos conteúdos Python Pro: https://bit.ly/galera-python-pro
🗣 Fique por dentro de todas nossas novidades: https://bit.ly/canal-python-pro

---

Nós te mostraremos os motivos para você não ser um fullstack, as vantagens e quando se preocupar em fazer essa função.

---

🎧 Ouça o Podcast DevPro: https://t.ly/XGM2w

👤 Siga-nos nas Redes sociais:
👉🏻 Instagram: https://instagram.com/renzoprobr
👉🏻 Twitter: https://twitter.com/renzoprobr
👉🏻 Facebook: https://www.facebook.com/pythonprobr
👉🏻 Linkedin: https://www.linkedin.com/in/renzonuccitelli/

🐍 Conheça o Python Pro!
👉🏻 Python Pro: http://python.pro.br"""

descricao_antiga_errada = """Descrição Youtube:

✅ Quer aprender Python? Eu preparei um curso rápido e grátis pra você! Cadastre-se no link:
http://bit.ly/curso-basico-de-python-...

✅ Curso para de programação intermediário:
http://bit.ly/curso-de-programacao-in...

🗣 Grupo de discussão dos conteúdos Python Pro: https://bit.ly/galera-python-pro
🗣 Fique por dentro de todas nossas novidades: https://bit.ly/canal-python-pro

---

Nós te mostraremos os motivos para você não ser um fullstack, as vantagens e quando se preocupar em fazer essa função.

---

🔊 Ouça na sua plataforma preferida!

👉🏻 Link para o podcast no Youtube: https://t.ly/XGM2w
👉🏻 Link para o podcast no Spotify: https://spoti.fi/2M0BvlG
👉🏻 Link para o podcast no Google Podcasts: https://bit.ly/2IBuZ2s
👉🏻 Link para o podcast no Anchor FM: https://anchor.fm/devpro
👉🏻 Link para o podcast no Breaker: https://www.breaker.audio/devprocast
👉🏻 Link para o podcast no Pocket Casts: https://pca.st/ik7tyb8g
👉🏻 Link para o podcast no RadioPublic: https://radiopublic.com/devprocast-6N...

👤 Redes sociais:
👉🏻 Instagram: https://instagram.com/renzoprobr
👉🏻 Twitter: https://twitter.com/renzoprobr
👉🏻 Facebook: https://www.facebook.com/pythonprobr
👉🏻 Youtube: https://www.youtube.com/user/renzonuc...
👉🏻 Linkedin: https://www.linkedin.com/in/renzonucc...

🐍 Conheça o Python Pro!
👉🏻 Python Pro: http://python.pro.br"""
