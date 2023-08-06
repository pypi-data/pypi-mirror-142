# abbrev_example.py
import argparse
from janda import Pururin
import asyncio
import json
import requests
import os
import re
import time

pururin = Pururin()

def input():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('--pururin', action='store', type=int)
    my_parser.add_argument('--id', action='store', type=int)

    args = my_parser.parse_args()
    return args


async def get_pur(id: int = input().pururin):
    data = await pururin.get(id)
    parser = json.loads(data)
    jdl = parser['title']
    teg = parser['tags']
    jdl = re.sub(r'[^\w\s]','', jdl)
    print(f'Title: {jdl}')

    img = parser['images']
    print(f'Total image: {len(img)}')
    
    if not os.path.exists(jdl):
        os.makedirs(jdl)

    if len(img) == len(os.listdir(jdl)):
        print("All images already downloaded! If you're doubt kindly remove this folder and re-download")
        return

    for i in img:
        start = time.time()
        ##print(i)
        img_url = i
        ## remove everything before the last /
        img_name = img_url.rsplit('/', 1)[-1]

        r = requests.get(img_url)
        with open(jdl + '/' + img_name, 'wb') as f:
            
            f.write(r.content)
            ## show write progress
            ## print(f'Downloading {img_url} => {img_name}')
     
            if os.path.exists(jdl + '/' + img_name):
                ## time.time() - start
                print(f'Successfully downloaded {img_name} | in {time.time() - start:.2f} seconds')
            
            ## jika semua sudah terdownload, maka print sukses
            if len(img) == len(os.listdir(jdl)):
                print("All images downloaded!")
                return