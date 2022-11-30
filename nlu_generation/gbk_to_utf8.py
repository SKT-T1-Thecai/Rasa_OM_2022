import os

file = './output/train/'
for f_src in os.listdir(file):
    #print(f_src)
    #print(f_src.split('.')[0:-1].c)
    # print(os.path.splitext(f_src)[-1])
    tgt_name = f_src.replace(".json",".utf8.json")
    with open(file+f_src,"r",encoding="gbk") as src:
        content = src.read()
        src.close()
        with open(file+tgt_name,"w",encoding="utf-8") as tgt:
            tgt.write(content)
            tgt.close()

