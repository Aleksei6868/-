import requests

import data
import configuration


def post_new_order():
    return requests.post(configuration.URL + configuration.PATH,
                        json=data.body).json()["track"]



def check_order():
    return requests.get(configuration.URL + configuration.PATH_GET + str(post_new_order()))


