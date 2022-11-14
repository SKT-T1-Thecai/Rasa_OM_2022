import pandas as pd
xlsx_path = "D:\PycharmProjects\OM_data\mini\csv\plat_scheme.xlsx"
xlsx = pd.read_excel(xlsx_path,sheet_name="设备互联")
network_data = []
names = set()
for i in xlsx.index.values:
    row_data = xlsx.loc[i, ['源设备名称', '源设备所在机房', '源设备所在机柜', '源设备机柜位置(U)', '目标设备名称', '目标设备所在机房', '目标设备所在机柜', '目标设备机柜位置(U)', '源设备序列号', '源设备类型', '目标设备序列号', '目标设备类型', '源设备端口', '目标设备端口']
].to_dict()
    network_data.append(row_data)
    names.add(row_data["目标设备类型"])
# print(len(network_data))
print(names)
