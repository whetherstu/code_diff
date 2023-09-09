import re
from collections import *
import os
import pandas as pd


def getOpcodeSequence(filename):  # 获取操作码序列
    opcode_seq = []
    # 将字符串引出为一个pattern模式
    p = re.compile(r'\s([a-fA-F0-9]{2}\s)+\s*([a-z]+)')
    with open(filename, mode="r", encoding='utf-8', errors='ignore') as f:
        for line in f:
            if line.startswith(".text"):
                m = re.findall(p, line)
                if m:
                    opc = m[0][1]
                    if opc != "align":
                        opcode_seq.append(opc)
    return opcode_seq


def getOpcodeNgram(ops, n=3):  # 将操作码序列以3个操作码为单位切片，并统计各个单位序列
    opngramlist = [tuple(ops[i:i + n]) for i in range(len(ops) - n)]
    opngram = Counter(opngramlist)
    return opngram


basepath = "E:\\big\\subtrain\\"
map3gram = defaultdict(Counter)
subtrain = pd.read_csv('E:\\big\\subtrainLabels.csv')
count = 1

for sid in subtrain.Id:  # 获取每个文件的n-gram特征并存入map3gram中
    print("counting the 3-gram of the {0} file...".format(str(count)))
    count += 1
    filename = basepath + sid + ".asm"
    ops = getOpcodeSequence(filename)
    op3gram = getOpcodeNgram(ops)
    map3gram[sid] = op3gram


cc = Counter([])  # 获取总的n-gram特征，计算其出现的次数，将出现次数大于500的
for d in map3gram.values():  # 单位存入selectedfeatures中用于后面的处理
    print(d)
    cc += d
selectedfeatures = {}
tc = 0
for k, v in cc.items():
    if v >= 500:
        selectedfeatures[k] = v
        print(k, v)
        tc += 1

dataframelist = []
for fid, op3gram in map3gram.items():  # 每个文件的n-gram特征为dataframelist中的一行，每一列为各单位出现的次数
    standard = {}
    standard["Id"] = fid
    for feature in selectedfeatures:
        if feature in op3gram:
            standard[feature] = op3gram[feature]
        else:
            standard[feature] = 0
    dataframelist.append(standard)

df = pd.DataFrame(dataframelist)
df.to_csv("E:\\big\\3gramfeature.csv", index=False)