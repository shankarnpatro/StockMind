import os

import requests

API_ENDPOINT = 'http://192.168.1.18:8000/api/users/2/profile_image/'
token = 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6IjU0MzIxNjc4OTAiLCJleHAiOjE1NTY2NzUzOTIsIm9yaWdfaWF0IjoxNTU2NjIzNTUyfQ.faHAknhtt3mEdhWkceRdv8fgSdMjSKos_rK32OWS7ls'
image_path = r'C:\Users\Shankar\Downloads\Images\FinalLogo.png'


def send_image_to_server(image_path):
    """

    :param image_path:
    :return:
    """

    image_filename = os.path.basename(image_path)
    print(image_filename)
    multipart_form_data = {'image': (image_filename, open(image_path, 'rb'))}
    r = requests.put(url=API_ENDPOINT, files=multipart_form_data, headers={'authorization': token})
    print(r.status_code)


send_image_to_server(image_path)
