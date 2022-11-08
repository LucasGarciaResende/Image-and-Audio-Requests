import requests
from file_check import format_check
from tk_window import req_window, error_window

reqs = req_window()
link = reqs[0]
image_name = reqs[1]
pic_req = requests.get(link)
if pic_req.status_code == 200:
    with open(f"{image_name}{format_check(link)}", 'wb') as f:
        f.write(pic_req.content)
else:
    error_window(pic_req.status_code)