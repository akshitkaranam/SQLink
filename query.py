from utils.plan import get_qep_nodes

if __name__ == '__main__':

    disable = tuple(["hashjoin"])
    list_scan, list_join = get_qep_nodes(5, disable)



    for node in list_scan:
        # print(node.__repr__())
        print(node.node_type, node.relation_name)

    print()
    print()
    for node in list_join:
        # print(node)
        # print(node.node_type)
        if node.node_type == "HASH JOIN":
            print(node.node_type, node.hash_condition)
        elif node.node_type == "MERGE JOIN":
            print(node.node_type, node.merge_condition)
        elif node.node_type == "NESTED LOOP":
                print(node.node_type, node.join_filter)
        else: print(node.node_type)
            
