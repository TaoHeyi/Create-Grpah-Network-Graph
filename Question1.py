import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import random


#####################The codes below here is to collect data#####################

# current colums are influencer_name, follower_id, follower_name
cols = [1, 5]
df = pd.read_csv('influence_data.csv', usecols=cols)

influenced_numbers = {}
#Change the number 15000 to choose how many rows you want to take consider in the graph
number = 1500

'''
randomlist = []
for i in range(number):
    n = random.randint(0, 42772)
    randomlist.append(n)
'''

for i in range(number):
    if(df['influencer_name'][i] not in influenced_numbers.keys()):
        influenced_numbers[df['influencer_name'][i]] = 0
    influenced_numbers[df['influencer_name'][i]] += 1

top_people_list = []
#Change the number 30 to choose the number of people who have greates influence to other people on the graph(Green Dots)
temp = dict(sorted(influenced_numbers.items(), key=lambda item: item[1], reverse=True)[:10]).keys()
print("Number of people each person has influenced")
print(influenced_numbers)

for i in temp:
    top_people_list.append(i)
print(top_people_list)

#####################The codes below here is to draw the graph#####################
#Resize the plot here if the resolution is low
plt.figure(figsize=(40, 40))
G = nx.DiGraph()
for i in range(number):
    G.add_edge(df['influencer_name'][i], df['follower_name'][i])

labels = {}
for node in G.nodes():
    if node in top_people_list:
        labels[node] = node

pos = nx.spring_layout(G, k=1, iterations=130)
nx.draw_networkx(G, pos, arrows=True, font_size=7, font_color='purple', with_labels=True, node_size=200)
nx.draw_networkx_nodes(G, pos, labels, cmap=plt.get_cmap('jet'), node_size=300, node_color='g')
nx.draw_networkx_labels(G, pos, labels, font_size=7, font_color='r')

plt.show()

