#input cell
large=1000000
 
#taking Evs as dictionary
Evs = {
    'P1' : {
        'source' : 'V1',
        'destination': 'V8',
        'init_battery' : 5,
        'charging' : 2,
        'discharging' : 3,
        'max' : 100,
        'speed' : 12
    },
    "P2": {
        "source": "V2",
        "destination": "V8",
        "init_battery": 20,
        "charging": 10,
        "discharging": 11,
        "max": 200,
        "speed": 20
    },
    "P3": {
        "source": "V3",
        "destination": "V6",
        "init_battery": 4,
        "charging": 1,
        "discharging": 2,
        "max": 120,
        "speed": 15
    },
    "P4": {
        "source": "V4",
        "destination": "V1",
        "init_battery": 4,
        "charging": 2,
        "discharging": 3,
        "max": 100,
        "speed": 12
 
    }
}

#the path graph as dictinary in form of adjency list
graph = {
    'V1' : {
        'V2' : 8,
        'V4' : 4,
        'V5' : 10
    },
    "V2": {
        "V1": 8,
        "V3": 4
    },
    "V3": {
        "V2": 4,
        "V4": 7,
        "V7": 6
    },
    "V4": {
        "V1": 4,
        "V3": 7,
        "V5": 8,
        "V7": 6
    },
    "V5": {
        "V1": 10,
        "V4": 7,
        "V6": 5
    },
    "V6": {
        "V5": 5,
        "V7": 1,
        "V8": 2
    },
    "V7": {
        "V3": 1,
        "V4": 4,
        "V6": 3,
        "V8": 5
    },
    "V8": {
        "V6": 2,
        "V7": 5
    }
}

# FUNCTION CELL 
cars = Evs.keys()     #defining cars as evs
cities = graph.keys()
for car in cars:
    Ev = Evs[car]
    max_dist = Ev['max']*Ev['discharging']             #the maximum distance a car can travel with max battery capacity         
    
    #initiating our search algorithm algorithm
    distances={}                                       #creating a dictionary which stores the shortest path distance between source node and a given node 
    parents={}                                        #creating dictionary for storing the parent node of every visited node
    iterate=[]                                        # creating a list of unvisited nodes(cities)
    for city in cities:                               
        distances[city]=large
        if(city!=Ev["source"]):
            iterate.append(city)
    distances[Ev["source"]]=0
    parents[Ev["source"]]=None
    
    n_cities = graph[Ev["source"]].keys()
    for n_city in n_cities:                                           #iterating to find the nearest city to the source node.
        parents[n_city]=Ev["source"]
        distances[n_city]=graph[Ev["source"]][n_city]
    while (len(iterate)):
        min=large
        mincity=None
        for city in iterate:
            dist= distances[city]
            if(dist<min):
                min=dist
                mincity=city                                            #storing nearest city from the source node in mincity
        iterate.remove(mincity)                                         #removing the mincity from the iterate list
        n_cities=graph[mincity].keys()
        for n_city in n_cities:                                      
            if (graph[mincity][n_city]>max_dist):                      #if the distance between two nodes is greater than maxdistance 
                pass                                                   #that a car can traverse with initial battery status then return. 
            upd=min+graph[mincity][n_city]              
            if (upd < distances[n_city]):                               # updating the shortest distance of the node from source in the distances dictionary
                distances[n_city]=upd
                parents[n_city]=mincity
    pathlist = []                                                       #creating the pathlist to store optimal path for each EV
    chain=Ev['destination']
    #code joining chain with parents
    while(chain!= None):        
                pathlist.append(chain)
                chain = parents[chain]
                time=0                                                          # updating  time taken through optimal path
                time=time+ (distances[Ev['destination']]/Ev['speed']) 
                req_battery= (distances[Ev['destination']]/Ev['discharging']) - Ev['init_battery'] 
                if(req_battery>0):
                  time = time + req_battery/Ev['charging']               

    path_list = pathlist[::-1]  
    print(path_list)
    print(time)
    

    

['V1', 'V4', 'V7', 'V8']
1.25
['V2', 'V3', 'V7', 'V8']
0.75
['V3', 'V7', 'V6']
1.1
['V4', 'V1']
0.3333333333333333
