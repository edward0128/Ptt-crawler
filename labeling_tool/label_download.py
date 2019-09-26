from __future__ import print_function
from argparse import ArgumentParser
parser = ArgumentParser()

parser.add_argument("json", help="labeling json file")
parser.add_argument("-d", "--dest", help="dataset directory path", dest="dest", default="/tmp/")


args = parser.parse_args()
print("json file path:", args.json)
print("dataset path", args.dest)

import json
import requests
import os

with open(args.json, "r", encoding='utf-8')as f:
    dataset = json.load(f)

    print("downloading ...")
for element in dataset:

    path =args.dest
    path +="/"
    path += element['Project Name']
    path +="/"
    path += element['Label']['flower']
    path +="/"
    if not os.path.isdir(path):
     os.makedirs(path)

    path += element['External ID']

    print ("ProjectName:"+element['Project Name']+"   "+"LabelName:"+element['Label']['flower'])
    print (element['External ID'])

    #get data url
    url = element['Labeled Data']
    print (url)
    r=requests.get(url)
    with open(path,'wb') as f:
        f.write(r.content)

print("download success ...")




