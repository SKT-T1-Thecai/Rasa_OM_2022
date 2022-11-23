from py2neo import Graph


class PlatformScheme():
    def __init__(self):
        self.neo4j_link =Graph(
            host="127.0.0.1",
            port=7687,
            user="neo4j",
            password="123456"
        )

    def get_bussiness_system_by_name(self,business_system):
        query = "match (p:business_system) where p.name =\"" + business_system + "\" return p"
        result = self.neo4j_link.run(query)
        return result.data()[0]["p"]

    def get_virtual_machines_of_business_system(self,business_system):
        query = "match (p:virtual_machine) where p.business_system=\"" + business_system + "\" return p"
        result = self.neo4j_link.run(query)
        # print(result.data())
        res = []
        for node in result.data():
           res.append(node["p"])
        return res
    def get_host_machine_of_business_system(self,business_system):
        query = "match (p:virtual_machine) where p.business_system=\"" + business_system + "\" return p"
        result = self.neo4j_link.run(query)
        data = result.data()
        if len(data)==0:
            return -1
        else:
            # 待修改
            host_machine_seq_number = data[0]["p"]["host_machine_seq_number"]
            query_1 = "match (p:host_machine) where p.seq_number=\"" + host_machine_seq_number + "\" return p"
            result_1 = self.neo4j_link.run(query_1)
            data_1 = result_1.data()
            if len(data_1)==0:
                return -1
            res = {"host_name":data_1[0]["p"]["host_name"],
                   "seq_number":data_1[0]["p"]["seq_number"]}
            print(res)
            return res


p = PlatformScheme()
#p.get_virtual_machines_of_business_system("社会应急力量管理系统")
p.get_host_machine_of_business_system("社会应急力量管理系统")