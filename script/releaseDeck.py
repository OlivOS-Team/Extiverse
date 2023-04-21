import json
import os
import shutil
from urllib import parse

if __name__ == '__main__':
    index_data = {}
    deck_user_list = os.listdir('../deck/')
    deck_meta_list = ['index.json']
    for deck_meta_list_this in deck_meta_list:
        if deck_meta_list_this in deck_user_list:
            deck_user_list.pop(deck_user_list.index(deck_meta_list_this))
    for deck_user_this in deck_user_list:
        for deck_type in [
            'classic'
        ]:
            index_data.setdefault(deck_type, [])
            meta_info_data = None
            file_dir_path = f'../deck/{deck_user_this}/{deck_type}/'
            file_dir_path_real = f'deck/{deck_user_this}/{deck_type}/'
            file_meta_info_path = f'../deck/{deck_user_this}/{deck_type}/__index.json'
            if os.path.exists(file_meta_info_path):
                with open(file_meta_info_path, 'r', encoding='utf-8') as f:
                    meta_info_data = json.loads(f.read())
            if type(meta_info_data) is not dict:
                meta_info_data = {}
            if os.path.exists(file_dir_path):
                deck_name_list = os.listdir(file_dir_path)
                deck_name_meta_list = ['__index.json']
                for deck_name_meta_this in deck_name_meta_list:
                    if deck_name_meta_this in deck_name_list:
                        deck_name_list.pop(deck_name_list.index(deck_name_meta_this))
                for deck_name_this in deck_name_list:
                    deck_name = deck_name_this
                    if deck_name.endswith('.json'):
                        deck_name = deck_name.rstrip('.json')
                    elif deck_name.endswith('.json5'):
                        deck_name = deck_name.rstrip('.json5')
                    info_this = {
                        "name": meta_info_data.get(deck_name_this, {}).get('name', deck_name),
                        "version": meta_info_data.get(deck_name_this, {}).get('version', '1'),
                        "version_code": meta_info_data.get(deck_name_this, {}).get('version_code', 1),
                        "desc": meta_info_data.get(deck_name_this, {}).get('desc', ''),
                        "download_link": 'https://raw.githubusercontent.com/OlivOS-Team/Extiverse/main/%s%s' % (
                            file_dir_path_real,
                            parse.quote(deck_name_this)
                        ),
                        "path": file_dir_path_real + deck_name_this,
                        "author": meta_info_data.get(deck_name_this, {}).get('author', deck_user_this),
                        "type": "deck",
                        "sub_type": deck_type
                    }
                    index_data[deck_type].append(info_this)
    os.makedirs('../target/deck/', exist_ok=True)
    with open('../target/deck/index.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(index_data, indent=4, ensure_ascii=False))
    shutil.copyfile('../target/deck/index.json', '../deck/index.json')
