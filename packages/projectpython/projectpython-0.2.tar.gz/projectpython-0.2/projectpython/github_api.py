import requests


def buscar_avatar(usuario):
    """
    busca o avatar de um usuario no github

    :param usuario: str com link do avatar
    :return:
    """

    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('renzon'))
