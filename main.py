# 3rd Quarter Project
from pyscript import display, document


def list_of_players(e):
    document.getElementById('output').innerHTML = ' '

    players_list = ['Escudero', 'Estrada', 'Tolentino', 'Pimentel', 'Binay', 'Cayetano', 'Dela Rosa', 'Ejercito', 'Gatchalian', 'Go', 'Hontiveros', 'Lapid', 'Legarda', 'Marcos', 'Padilla', 'Poe', 'Revilla', 'Tulfo', 'Villanueva', 'Villar', 'Zubiri']
    bullet = 1

    for players in players_list:
        display(f'{bullet}) {players}', target='output')
        bullet = bullet++1
