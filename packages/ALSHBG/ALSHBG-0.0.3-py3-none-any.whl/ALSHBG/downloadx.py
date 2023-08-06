import requests

class download:
    def YouTube(self,url):
        data = {'url':url, 'extension':'mp3'}
        BG = requests.post(f"https://onlinevideoconverter.pro/api/convert?url={url}", data=data).json()
        return BG