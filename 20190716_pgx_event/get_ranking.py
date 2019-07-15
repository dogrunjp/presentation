import csv
import networkx as nx
import random
from gensim.models import Word2Vec as word2vec


wiki_page_id = "2809541"
sample_size = 10


def label(str):
    label_str = str.split(":")
    return label_str[1]

def make_random_walks(G, num_of_walk, length_of_walk):
    walks = list()
    for i in range(num_of_walk):
        node_list = list(G.nodes())
        for node in node_list:
            # node idをwalkに追加するブロック
            now_node = node
            walk = list()
            walk.append(str(node))
            for j in range(length_of_walk):
                lst = list(G.neighbors(now_node))
                # IndexError: Cannot choose from an empty sequence が
                # random.choice()で発生するため。要fix！
                if len(lst)==0:
                    pass
                else:
                    next_node = random.choice(lst)
                    walk.append(str(next_node))
                    now_node = node
            walks.append(walk)
    return walks


def convert_id2artist(i):
    return [x for x in labels if x["id"]==i]


def convert_id2artist(i):
    return [x for x in labels if x["id"]==i]


input_file = "../output/artist2artist/artist2artist.pg"
f = open(input_file, mode="r")

reader = csv.reader(f, delimiter="\t")
# NetworkXにGraph.add_node()できるノードに変換
nodes = [(r[0], {"label":label(r[2])}) for r in reader if r[1]==":page_id"]
f.seek(0)
# NetworkXに読み込める属性付きエッジに変換
edges = [(r[0], r[2], {"property": r[3]}) for r in reader if r[1]=="->"]


G = nx.DiGraph()
# ノードを追加
G.add_nodes_from(nodes)
# エッジを追加
G.add_edges_from(edges)


walks = make_random_walks(G, 20, 20)
model = word2vec(walks, min_count=0, size=2, window=5, workers=1)


vector = model.wv[wiki_page_id]
ranking = model.wv.most_similar([vector], [], sample_size)


labels = [{"id":x[0],"label": x[1]["label"]} for x in nodes]


for e in ranking:
    page_id = e[0]
    artist_name = convert_id2artist(page_id)
    print(artist_name)

