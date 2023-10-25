from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError
import sys
import logging
import requests as req
import os

g_secret_id = ''
g_secret_key = ''
g_region = 'ap-shanghai'
g_Bucket = 'extiverse-1253866028'

if len(sys.argv) >= 2:
    g_secret_id = sys.argv[1]
if len(sys.argv) >= 3:
    g_secret_key = sys.argv[2]

def GETHttpFile(url, path):
    res = False
    send_url = url
    headers = {}
    try:
        msg_res = req.request("GET", send_url, headers = headers)
        with open(path, 'wb+') as tmp:
            tmp.write(msg_res.content)
        if msg_res.status_code in [200, 300]:
            res = True
        else:
            res = False
    except:
        res = False
    return res

def upload(src, dst):
    global g_secret_id, g_secret_key, g_region, g_Bucket
    secret_id = g_secret_id
    secret_key = g_secret_key
    region = g_region
    token = None
    config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token)
    client = CosS3Client(config)
    object_key = dst
    with open(src, 'rb') as fp:
        response = client.put_object(
            Bucket=g_Bucket,
            Body=fp,
            Key=object_key,
            EnableMD5=True,
            StorageClass='STANDARD',
            ContentType='text/html; charset=utf-8'
        )
    print(response['ETag'])

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

def file_name(file_dir):
    res = []
    for root,dirs,files in os.walk(file_dir):
        for file in files:
            res.append(os.path.join(root.lstrip(file_dir), file))
    return res

if __name__ == '__main__':
    res = file_name('../deck/')
    for res_this in res:
        print(res_this)
        upload(os.path.join('..', 'deck', res_this), os.path.join('deck', res_this).replace('\\', '/'))
