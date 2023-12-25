import json
import yaml
import os
import shutil
from urllib import parse
import codecs

dictMappping = {
    'classic': 'JSON',
    'yaml': 'YAML',
    'excel': 'XLSX'
}

dictCount = {
    'classic': 0,
    'yaml': 0,
    'excel': 0
}

def formatUTF8WithBOM(data:bytes):
    res = data
    if res[:3] == codecs.BOM_UTF8:
        res = res[3:]
    return res

if __name__ == '__main__':
    index_data = {}
    deck_user_list = os.listdir('../deck/')
    deck_meta_list = ['index.json']
    for deck_meta_list_this in deck_meta_list:
        if deck_meta_list_this in deck_user_list:
            deck_user_list.pop(deck_user_list.index(deck_meta_list_this))
    for deck_user_this in deck_user_list:
        for deck_type in [
            'classic',
            'yaml',
            'excel'
        ]:
            index_data.setdefault(deck_type, [])
            meta_info_data = None
            file_dir_path = f'../deck/{deck_user_this}/{deck_type}/'
            file_dir_path_real = f'deck/{deck_user_this}/{deck_type}/'
            deck_user_this_quote = parse.quote(deck_user_this)
            file_dir_path_real_quote = f'deck/{deck_user_this_quote}/{deck_type}/'
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
                    file_deck_info_path = f'../deck/{deck_user_this}/{deck_type}/{deck_name_this}'
                    deck_name = deck_name_this
                    if 'classic' == deck_type:
                        if deck_name.endswith('.json'):
                            deck_name = deck_name.rstrip('.json')
                        elif deck_name.endswith('.json5'):
                            deck_name = deck_name.rstrip('.json5')
                    elif 'yaml' == deck_type:
                        if deck_name.endswith('.yaml'):
                            deck_name = deck_name.rstrip('.yaml')
                    elif 'excel' == deck_type:
                        if deck_name.endswith('.xlsx'):
                            deck_name = deck_name.rstrip('.xlsx')
                        elif deck_name.endswith('.xls'):
                            deck_name = deck_name.rstrip('.xls')
                    deck_url_path_this = file_dir_path_real_quote + parse.quote(deck_name_this)
                    info_this = {
                        'name': meta_info_data.get(deck_name_this, {}).get('name', deck_name),
                        'download_link': [
                            f'https://extiverse-1253866028.cos.ap-shanghai.myqcloud.com/{deck_url_path_this}',
                            f'https://api.oliva.icu/extiverse/{deck_url_path_this}',
                            f'https://fastly.jsdelivr.net/gh/OlivOS-Team/Extiverse@main/{deck_url_path_this}',
                            f'https://ghproxy.com/https://github.com/OlivOS-Team/Extiverse/blob/main/{deck_url_path_this}',
                            f'https://raw.githubusercontent.com/OlivOS-Team/Extiverse/main/{deck_url_path_this}',
                        ],
                        'path': file_dir_path_real + deck_name_this,
                        'author': meta_info_data.get(deck_name_this, {}).get('author', deck_user_this),
                        'type': 'deck',
                        'sub_type': deck_type,
                        'resource_link': [
                            f'https://extiverse-1253866028.cos.ap-shanghai.myqcloud.com/deck/{deck_user_this_quote}/resource/' + parse.quote(deck_resource_this)
                            for deck_resource_this in meta_info_data.get(deck_name_this, {}).get('resource', [])
                        ]
                    }
                    if 'yaml' == deck_type:
                        pass
                        try:
                            with open(file_deck_info_path, 'rb') as customDeckPath_f:
                                obj_Deck_this = yaml.load(
                                    formatUTF8WithBOM(customDeckPath_f.read()).decode('utf-8'),
                                    Loader = yaml.FullLoader
                                )
                            if type(obj_Deck_this) is dict:
                                if 'author' in obj_Deck_this:
                                    info_this['author'] = str(obj_Deck_this['author'])
                                if 'version' in obj_Deck_this:
                                    info_this['version'] = str(obj_Deck_this['version'])
                                    try:
                                        info_this['version_code'] = int(obj_Deck_this['version'])
                                    except:
                                        pass
                                if 'desc' in obj_Deck_this:
                                    info_this['desc'] = str(obj_Deck_this['desc'])
                        except:
                            pass
                    info_this.setdefault('desc', meta_info_data.get(deck_name_this, {}).get('desc', ''))
                    info_this.setdefault('version', meta_info_data.get(deck_name_this, {}).get('version', '1'))
                    info_this.setdefault('version_code', meta_info_data.get(deck_name_this, {}).get('version_code', 1))

                    info_this_new = {}
                    for info_this_key in ['name', 'version', 'version_code', 'desc', 'download_link', 'path', 'author', 'type', 'sub_type']:
                        if info_this_key in info_this:
                            info_this_new[info_this_key] = info_this[info_this_key]
                    info_this_new.update(info_this)
                    index_data[deck_type].append(info_this_new)
            index_data[deck_type].sort(key=lambda x: x['name'])
    os.makedirs('../target/deck/', exist_ok=True)
    with open('../target/deck/index.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(index_data, indent=4, ensure_ascii=False))
    shutil.copyfile('../target/deck/index.json', '../deck/index.json')
    print('releaseDeck done!')

    for typeName in dictCount:
        str_this = f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="130" height="20" role="img" aria-label="JSON">
	<title>test: test</title>
	<linearGradient id="s" x2="0" y2="100%">
		<stop offset="0" stop-color="#bbb" stop-opacity=".1"/>
		<stop offset="1" stop-opacity=".1"/>
	</linearGradient>
	<clipPath id="r">
		<rect width="80" height="20" rx="10" fill="#fff"/>
	</clipPath>
	<g clip-path="url(#r)">
		<rect width="40" height="20" fill="#555"/>
		<rect x="40" width="130" height="20" fill="#007ec6"/>
		<rect width="130" height="20" fill="url(#s)"/>
	</g>
	<g fill="#fff" text-anchor="middle" font-family="Verdana,Geneva,DejaVu Sans,sans-serif" text-rendering="geometricPrecision" font-size="110">
		<text aria-hidden="true" x="210" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="">{dictMappping.get(typeName, "N/A")}</text>
		<text x="210" y="140" transform="scale(.1)" fill="#fff" textLength="">{dictMappping.get(typeName, "N/A")}</text>
		<text aria-hidden="true" x="580" y="150" fill="#010101" fill-opacity=".3" transform="scale(.1)" textLength="">{dictCount.get(typeName, "N/A")}</text>
		<text x="580" y="140" transform="scale(.1)" fill="#fff" textLength="">{dictCount.get(typeName, "N/A")}</text>
	</g>
</svg>
'''
        with open(f'../target/deck/{typeName}.svg', 'w', encoding='utf-8') as f:
            f.write(str_this)

    print('releaseSvg done!')
