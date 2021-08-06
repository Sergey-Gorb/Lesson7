import os
import pathlib
from collections import defaultdict

dic_f = defaultdict(list)
p = pathlib.Path('.')
for f_name in p.cwd().rglob('*.txt'):
    with open(f_name, 'r', encoding='UTF-8') as f:
        bas_name = os.path.basename(f_name)
        for st_r in f.readlines():
            dic_f[bas_name].append(sr_r.strip())
        for tup in (sorted([len(l_d), k, l_d]) for k, l_d in dic_f.items()):
            for s_w in tup[2]:
                print(s_w)
