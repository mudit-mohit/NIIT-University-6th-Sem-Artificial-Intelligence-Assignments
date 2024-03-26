import re
from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


def extract_entities(sentence):
    entities = re.findall(r'\b([A-Za-z]+)\b', sentence)
    return entities


def resolve_pronouns(sentence, entities):
    resolved_sentence = sentence
    for entity in entities:
        if entity.lower() == 'he' or entity.lower() == 'she':
            resolved_sentence = resolved_sentence.replace(entity, entities[-1])
    return resolved_sentence


def identify_relationships(sentence, entities):
    relationships = []
    verbs = re.findall(r'\bis\b|\bwas\b|\bwere\b|\bhas\b|\bhave\b|\bhad\b|\bannounced\b|\bpraised\b|\bbaked\b|\bchased\b|\bwent\b|\bbought\b', sentence)
    for verb in verbs:
        parts = re.split(verb, sentence)
        if len(parts) == 2:
            relationships.append((parts[0].strip(), verb.strip(), parts[1].strip()))
    return relationships


def create_multigraph(entities, relationships):
    G = nx.MultiGraph()
    for entity in entities:
        G.add_node(entity)
    for rel in relationships:
        G.add_edge(rel[0], rel[2], label=rel[1])
    return G


sentences = [
    "John went to the store to buy groceries.",
    "Sarah and David are best friends since childhood.",
    "The cat chased the mouse around the house.",
    "The company announced a new partnership with a tech firm.",
    "She baked a delicious cake for her sister's birthday.",
    "The teacher praised the students for their hard work."
]


all_entities = []
all_relationships = []
for sentence in sentences:
    entities = extract_entities(sentence)
    resolved_sentence = resolve_pronouns(sentence, entities)
    relationships = identify_relationships(resolved_sentence, entities)
    all_entities.extend(entities)
    all_relationships.extend(relationships)


all_entities = list(set(all_entities))
all_relationships = list(set(all_relationships))


G = create_multigraph(all_entities, all_relationships)


pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=10, font_weight='bold')
edge_labels = {(u, v): d['label'] for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.show()
