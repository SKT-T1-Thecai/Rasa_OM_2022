from data_import.import2neo4j import GraphMaker
from py2neo import Graph, Node
clean_all = "MATCH (r) DETACH DELETE r"
A = GraphMaker()
A.neo4j_link.run(clean_all)
# node1 = Node("student",name="张三")
# node2 = Node("student",name="李四",id="12345")
# node3 = Node("teacher",name="张华",id="T45")
# A.neo4j_link.create(node1)
# A.neo4j_link.create(node2)
# A.neo4j_link.create(node3)
# query = "match (p:%s),(q:%s) where p.name='%s' and q.name = '%s' create (p)-[rel:%s{name:'%s'}]->(q)"%\
#         ("teacher","student","张华","张三","教授","asdfasdf")
# A.neo4j_link.run(query)