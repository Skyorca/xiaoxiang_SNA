# Read the edge list and calculate the degrees of nodes

filename = r"F:\xiaoxiang_proj\sns_datasets\karate\karate_edges.txt"
mydict = {}
with open(filename) as f:
    for line in f.readlines():
        temp_list = line.split()
        start = temp_list[0]
        end = temp_list[1]

        if( start not in mydict ): mydict[start]=0
        if( end not in mydict ): mydict[end] = 0
        mydict[start] += 1
        mydict[end] += 1
        
print(mydict)