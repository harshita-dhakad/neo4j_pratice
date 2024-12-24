from py2neo import Graph, Node
graph = Graph("bolt://localhost:7687", auth=("neo4j", "Ritik@123"))



def update_node_into_neo4j(label_name:str,props:list, id:int) :
    try :
        label = label_name[0].upper() + label_name[1:].lower()
        node = Node(label, id=id)  
        graph.merge(node, label, "id")

        for key, value in props.items():
            node[key] = value  

        graph.push(node)
    except Exception as err :
        print(err)
        


update_node_into_neo4j('employee', {"name" : "punit", "age" : 16, "email" : "ritik@gmail.com"}, 20)