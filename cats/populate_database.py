import requests 

import base64
import json


url = "https://api.nabeelzar.com/cat/"
image_file = "19.png"

with open(image_file, "rb") as f:
	im_bytes = f.read()

# im_b64 = base64.b64encode(im_bytes).decode("utf-8")
headers = {'Content-type': 'application/json', 'Accept': 'multipart/form-data'}

# payload = json.dumps({"source_name": "hello", "img_path": im_b64})
payload = {"source_name": "hello", "img_path": im_bytes}
payload = {"source_name": "hello",}

files=[
  ('img_path',("1.png", open(image_file,'rb'),'image/png'))
]
# res = requests.post(url, data=payload, headers=headers)
res = requests.post(url, data=payload, files=files, headers=headers)

print(res)