import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {self.token}'}
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        #new_path = file_path.replace("\\", "/")
        list_path = file_path.split('\\')
        res = requests.get(f'{URL}/upload?path={list_path[-1]}&overwrite=true', headers=headers).json()
        with open(file_path, 'rb') as f:
            try:
                result = requests.put(res['href'], files={'file':f})
                print(result)
            except KeyError:
                print(res)

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = input('Введите путь к файлу: ')
    token = input('Введите токен: ')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)