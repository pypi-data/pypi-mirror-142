import requests

# TODO: adapt host based on project
HOST = 'https://www.sky.top/'


class Model:

    def __init__(self, name) -> None:
        self.name = name
        self.base_url = HOST + name

    def create(self, data):
        url = self.base_url
        response = requests.post(url, data=data)
        return response

    def delete(self, id):
        url = self.base_url + '/' + id
        response = requests.delete(url)
        return response

    def get(self, id):
        url = self.base_url + '/' + id
        response = requests.get(url)
        return response

    def list(self):
        # TODO: filters
        url = self.base_url
        response = requests.get(url)
        return response

    def update(self, id, data):
        url = self.base_url + '/' + id
        response = requests.put(url, data=data)
        return response

    # TODO: websockets
    def send(self):
        raise NotImplementedError

    def listen(self):
        raise NotImplementedError
