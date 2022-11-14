from py2neo import Graph, Node
import json
from tqdm import tqdm
json_folder = "D:\PycharmProjects\OM_data\\new\JSON\\"
file_list = ["业务系统.json",
             "虚拟机.json",
             "数据库.json",
             "中间件.json",
             "宿主机.json",
             "设备互联.json",
             "网络设备.json"]
labels = ["business_system","virtual_machine","database",
          "middleware","host_machine","link","network_device"]
def process(folder,file_list):
    data = []
    for file in file_list:
        path =  folder+file
        single_file = json.load(open(path,"r",encoding="UTF-8"))
        data.append({"label":file.split(".")[0],"data":single_file})
    return data
class GraphMaker(object):
    def __init__(self):
        self.neo4j_link =Graph(
            host="127.0.0.1",
            port=7687,
            user="neo4j",
            password="123456"
        )
    # 创建节点需要节点的label（1/8），节点的数据
    def create_nodes(self,data):
        self.neo4j_link.run("MATCH (r) DETACH DELETE r")
        for line in tqdm(enumerate(data)):
            label = labels[line[0]]
            data = line[1]["data"]
            # print(label)
            for item in data:
                if label=="business_system":
                    node = Node(label,name=item["name"],
                    system_type=item["system_type"],
                    department=item["department"],
                    department_director=item["department_director"],
                    manufactor=item["manufactor"],
                    manufactor_director=item["manufactor_director"],
                    system_status=item["system_status"],
                    online_time=item["online_time"],
                    department_type=item["department_type"])
                    self.neo4j_link.create(node)
                elif label=="virtual_machine":
                    # 把业务系统和ip合起来命名虚拟机
                    node = Node(label,name=item["business_system"]+item["server_ip"],
                    business_system=item["business_system"],
                    server_name=item["server_name"],
                    server_ip=item["server_ip"],
                    host_machine_seq_number=item["host_machine_seq_number"],
                    cloud_resource_center=item["cloud_resource_center"],
                    os_version=item["os_version"],
                    cpu_core_number=item["cpu_core_number"],
                    memory=item["memory"],
                    system_disk=item["system_disk"],
                    data_disk=item["data_disk"])
                    self.neo4j_link.create(node)
                elif label=="database":
                    node = Node(label,name=item["database_name"],
                    database_name= item["database_name"],
                    business_system= item["business_system"],
                    db_internal_ip= item["db_internal_ip"],
                    db_external_ip= item["db_external_ip"],
                    database_type= item["database_type"],
                    database_version= item["database_version"],
                    database_port= item["database_port"],
                    )
                    self.neo4j_link.create(node)
                elif label=="middleware":
                    node = Node(label,name=item["ip"]+"-"+item["port"],
                    business_system=item["business_system"],
                    ip= item["ip"],
                    middleware_type= item["middleware_type"],
                    middleware_version= item["middleware_version"],
                    middleware_name= item["name"],
                    port= item["port"],
                    )
                    self.neo4j_link.create(node)
                elif label=="host_machine":
                    node = Node(label,name=item["seq_number"],
                    host_name=item["host_name"],
                    seq_number=item["seq_number"],
                    usage=item["usage"],
                    controller_ip=item["controller_ip"],
                    server_type=item["server_type"],
                    brand=item["brand"],
                    model=item["model"],
                    computer_room=item["computer_room"],
                    cabinet=item["cabinet"],
                    u_occupy_number=item["u_occupy_number"],
                    u_install_location=item["u_install_location"],
                    department=item["department"],
                    department_director=item["department_director"],
                    device_model=item["device_model"],
                    cpu_model=item["cpu_model"],
                    physical_cpu_number= item["physical_cpu_number"],
                    all_cpu_core_number= item["all_cpu_core_number"],
                    memory_specification= item["memory_specification"],
                    memory_capacity= item["memory_capacity"],
                    disk_capacity= item["disk_capacity"],
                    in_use= item["in_use"],
                    )
                    self.neo4j_link.create(node)
                elif label=="link":
                    node = Node(label,name=item["link_name"],
                    link_name= item["link_name"],
                    source_device_name= item["source_device_name"],
                    source_device_computer_name= item["source_device_computer_name"],
                    source_device_cabinet= item["source_device_cabinet"],
                    source_device_cabinet_location= item["source_device_cabinet_location"],
                    target_device_name= item["target_device_name"],
                    target_device_computer_name= item["target_device_computer_name"],
                    target_device_cabinet= item["target_device_cabinet"],
                    target_device_cabinet_location= item["target_device_cabinet_location"],
                    source_device_seq_number= item["source_device_seq_number"],
                    source_device_type= item["source_device_type"],
                    target_device_seq_number= item["target_device_seq_number"],
                    target_device_type= item["target_device_type"],
                    source_device_port= item["source_device_port"],
                    target_device_port= item["target_device_port"]
                                )
                    self.neo4j_link.create(node)
                elif label=="network_device":
                    node = Node(label,name=item["host_name"]+item["controller_ip"],
                    host_name=item["host_name"],
                    device_type=item["device_type"],
                    seq_number=item["seq_number"],
                    controller_ip=item["controller_ip"],
                    usage=item["usage"],
                    in_use=item["in_use"],
                    brand=item["brand"],
                    model=item["model"],
                    computer_room=item["computer_room"],
                    cabinet=item["cabinet"],
                    u_occupy_number=item["u_occupy_number"],
                    u_install_location=item["u_install_location"],
                    department_director=item["department_director"],
                    maintainer=item["maintainer"],
                    maintain_start_time=item["maintain_start_time"],
                    maintain_end_time=item["maintain_end_time"],
                    discription=item["discription"],
                    )
                    self.neo4j_link.create(node)
                else:
                    print("warning：出现了未定义的label")
    def get_data(self,data,label):
        for line in enumerate(data):
            if labels[line[0]]==label:
                return line[1]["data"]
        return None
    # 创建关系需要源节点和目标节点的类型和名称 以及关系的类型
    # 关系：业务系统->数据库
    #       业务系统->虚拟机
    #       业务系统->中间件
    #       虚拟机->宿主机
    #       设备->宿主机  设备是从宿主机/网络设备中抽象出来的
    #       设备->网络设备
    #       业务系统->虚拟机
    #       链路->设备

    def create_rels(self,data):
        self.neo4j_link.run("MATCH ()-[r]->()DELETE r")
        rels = []
        business_system_data = self.get_data(data,"business_system")
        virtual_machine_data = self.get_data(data,"virtual_machine")
        middleware_data = self.get_data(data,"middleware")
        database_data = self.get_data(data,"database")
        host_machine_data = self.get_data(data,"host_machine")
        network_device_data = self.get_data(data,"network_device")
        link_data = self.get_data(data,"link")
        # 获取关系： 业务系统 -> 虚拟机 verified
        for virtual_machine in virtual_machine_data:
            # rel = [virtual_machine["business_system"],
            #        virtual_machine["business_system"]+virtual_machine["server_ip"],"has_virtual_machine"]
            rel = {"start_node_type":"business_system",
                   "end_node_type":"virtual_machine",
                   "start_name":virtual_machine["business_system"],
                   "end_name":virtual_machine["business_system"]+virtual_machine["server_ip"],
                   "rel_type":"has_virtual_machine"}
            rels.append(rel)
        # 业务系统 -> 中间件 verified
        for middleware in middleware_data:
            rel = {"start_node_type":"business_system",
                   "end_node_type":"middleware",
                   "start_name":middleware["business_system"],
                   "end_name":middleware["ip"]+"-"+middleware["port"],
                   "rel_type":"has_middleware"}
            rels.append(rel)
        # 业务系统 -> 数据库 verified
        for database in database_data:
            rel = {"start_node_type":"business_system",
                   "end_node_type":"database",
                   "start_name":database["business_system"],
                   "end_name":database["database_name"],
                   "rel_type":"has_database"}
            rels.append(rel)
        # 虚拟机->宿主机 verified
        for virtual_machine in virtual_machine_data:
            rel = {"start_node_type":"virtual_machine",
                    "end_node_type":"host_machine",
                    "start_name":virtual_machine["business_system"]+virtual_machine["server_ip"],
                    "end_name":virtual_machine["host_machine_seq_number"],
                    "rel_type":"has_host_machine"}
            rels.append(rel)
        # 设备->宿主机 verified
        for host_machine in host_machine_data:
            if not host_machine["seq_number"]=="":
                rel = {"start_node_type": "device",
                       "end_node_type": "host_machine",
                       "start_name": host_machine["seq_number"],
                       "end_name": host_machine["seq_number"],
                       "rel_type": "is_real_pc"}
            rels.append(rel)
        # 设备->网络设备 verified
        for network_device in network_device_data:
            if not network_device["host_name"]=="未上架":
                rel = {"start_node_type": "device",
                       "end_node_type": "network_device",
                       "start_name": network_device["host_name"]+network_device["controller_ip"],
                       "end_name": network_device["host_name"]+network_device["controller_ip"],
                       "rel_type": "is_real_network_device"}
                rels.append(rel)
        # 链路->设备
        link_rels = []
        for link in link_data:
            link_rel = {"start_node_type": "link",
                   "end_node_type": "device",
                   "start_name": link["link_name"],
                   "end_name": link["source_device_seq_number"],
                   "rel_type": "link_source_device"}
            link_rels.append(link_rel)
            link_rel = {"start_node_type": "link",
                   "end_node_type": "device",
                   "start_name": link["link_name"],
                   "end_name": link["target_device_seq_number"],
                   "rel_type": "link_target_device"}
            link_rels.append(link_rel)
        for rel in rels:
            query = "match (p:%s),(q:%s) where p.name='%s' and q.name = '%s' create (p)-[rel:%s]->(q)"%\
         (rel["start_node_type"],rel["end_node_type"],rel["start_name"],rel["end_name"],rel["rel_type"])
            # print(query)
            # print(" ")
            print(query)
            self.neo4j_link.run(query)
        for link_rel in link_rels:
            query = "match (p:%s),(q:%s) where p.name='%s' and q.seq_number = '%s' create (p)-[rel:%s]->(q)"%\
         (link_rel["start_node_type"],link_rel["end_node_type"],
          link_rel["start_name"],link_rel["end_name"],link_rel["rel_type"])
            print(query)
            self.neo4j_link.run(query)





    def create_device_nodes(self,data):
        self.neo4j_link.run("match (p:device) delete p")
        for line in tqdm(enumerate(data)):
            label = labels[line[0]]
            data = line[1]["data"]
            if label=="host_machine":
                for item in data:
                    node = Node("device",name=item["seq_number"],
                    type="pc_machine",
                    host_name=item["host_name"],
                    seq_number=item["seq_number"],
                    usage=item["usage"],
                    controller_ip=item["controller_ip"],
                    server_type=item["server_type"],
                    brand=item["brand"],
                    model=item["model"],
                    computer_room=item["computer_room"],
                    cabinet=item["cabinet"],
                    u_occupy_number=item["u_occupy_number"],
                    u_install_location=item["u_install_location"],
                    department=item["department"],
                    department_director=item["department_director"],
                    device_model=item["device_model"],
                    cpu_model=item["cpu_model"],
                    physical_cpu_number= item["physical_cpu_number"],
                    all_cpu_core_number= item["all_cpu_core_number"],
                    memory_specification= item["memory_specification"],
                    memory_capacity= item["memory_capacity"],
                    disk_capacity= item["disk_capacity"],
                    in_use= item["in_use"],
                    )
                    self.neo4j_link.create(node)

            elif label=="network_device":
                for item in data:
                    node = Node("device",
                                type=item["device_type"],name=item["host_name"]+item["controller_ip"],
                                host_name=item["host_name"],
                                device_type=item["device_type"],
                                seq_number=item["seq_number"],
                                controller_ip=item["controller_ip"],
                                usage=item["usage"],
                                in_use=item["in_use"],
                                brand=item["brand"],
                                model=item["model"],
                                computer_room=item["computer_room"],
                                cabinet=item["cabinet"],
                                u_occupy_number=item["u_occupy_number"],
                                u_install_location=item["u_install_location"],
                                department_director=item["department_director"],
                                maintainer=item["maintainer"],
                                maintain_start_time=item["maintain_start_time"],
                                maintain_end_time=item["maintain_end_time"],
                                discription=item["discription"],
                                )
                    self.neo4j_link.create(node)
om_graph = GraphMaker()
data = process(json_folder,file_list)
om_graph.create_nodes(data)
om_graph.create_device_nodes(data)
om_graph.create_rels(data)






