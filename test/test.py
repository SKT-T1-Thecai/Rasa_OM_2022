from py2neo import Graph

p = "D:\PycharmProjects\Rasa_OM_2022\data\jieba_userdict\\business_system.txt"
p1 = "D:\PycharmProjects\Rasa_OM_2022\data\jieba_userdict\\business_system1.txt"
with open(p,"r",encoding="utf-8")as f:
    # print(f.readline().replace("\n","")+" 18000 nz")
    # print(f.readline())
    t = f.read().replace("\n"," 18000 nz\n")
    f.close()
    with open(p1,"w",encoding="utf-8")as f1:
        f1.write(t)
        f1.close()
