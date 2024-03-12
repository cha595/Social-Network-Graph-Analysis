import pandas as pd
from names import get_saved_names
import time

def get_mutuals(name):
    dd=[s.strip() for s in open(f'./mutuals/{name}_mutual.csv').readlines()]
    return dd

if __name__ == '__main__':

    st = time.time()
    all_names = [f.strip() for f in open('./all_names.csv').readlines()]
    
    # create matrix
    graph = pd.DataFrame(index=all_names, columns=all_names)
    graph.fillna('0', inplace=True)
    
    names = get_saved_names()

    for name in names: 
        try:
            mutuals=get_mutuals(name)
            for m in mutuals:
                graph.at[name,m]='1'
                graph.at[m,name]='1'
        except:
            pass
        
    graph.fillna('0', inplace=True)
    graph.to_csv('network.csv')
    ed = time.time()
    print(f'{ed-st}s to create the matrix.')
    print('saved to network.csv')

    #create adjacency list
    adj_list = {}
    for name in all_names:
        adj_list[name] = list(graph[graph[name] == '1'].index)
    with open('adj_list.json', 'w') as f:
        f.write(str(adj_list))
    print('saved to adj_list.json')
    print(f'{time.time()-ed}s to create the adjacency list.')
