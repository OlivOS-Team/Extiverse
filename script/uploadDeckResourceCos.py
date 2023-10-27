from qcloud_cos import CosConfig
from qcloud_cos import CosS3Client
from qcloud_cos import CosServiceError
from qcloud_cos import CosClientError
import sys
import logging
import requests as req
import os
import hashlib
import json

g_secret_id = ''
g_secret_key = ''
g_region = 'ap-shanghai'
g_Bucket = 'extiverse-1253866028'

if len(sys.argv) >= 2:
    g_secret_id = sys.argv[1]
if len(sys.argv) >= 3:
    g_secret_key = sys.argv[2]

def checkFileMD5(filePath):
    res = None
    if os.path.exists(filePath):
        with open(filePath, 'rb') as fp:
            fObj = fp.read()
            res = hashlib.md5(fObj).hexdigest()
    return res

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
    md5_dict = None
    res = file_name('../deck/')
    if os.path.exists('deck_md5.json'):
        with open('deck_md5.json', 'r', encoding='utf-8') as f:
            try:
                md5_dict = json.loads(f.read())
            except:
                pass
    if md5_dict is None:
        md5_dict = {}
    md5_dict_new = {}
    for res_this in res:
        res_md5_this = checkFileMD5(os.path.join('..', 'deck', res_this))
        res_md5_this_old = md5_dict.get(res_this, None)
        if res_md5_this_old != res_md5_this:
            print('File Change : %s : %s -> %s' % (res_this, res_md5_this_old, res_md5_this))
            upload(os.path.join('..', 'deck', res_this), os.path.join('deck', res_this).replace('\\', '/'))
        md5_dict_new[res_this] = res_md5_this
    with open('deck_md5.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(md5_dict_new, indent=4, ensure_ascii=False))
