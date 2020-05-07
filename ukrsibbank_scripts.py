import os
import re

source_folder = ''

pattern = re.compile(r"(?:from|join)[\s|\r]+[\w\.]+", re.IGNORECASE)
# sql = 'select * from \nf_oo where id in (select id jOin bar.df);'
# search = pattern.findall(sql)
# print(search)

for name in os.listdir(source_folder):
    if os.path.isfile(os.path.abspath(os.path.join(source_folder, name))):
        with open(name, 'r', encoding='utf-8') as f:
            sql = f.read()
            search = pattern.findall(sql)
            print(search)
