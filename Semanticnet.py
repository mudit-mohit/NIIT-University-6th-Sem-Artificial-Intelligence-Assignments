class SemanticNet:
    def __init__(self):
        self.entities = set()
        self.relations = {}

    def add_entity(self, entity):
        self.entities.add(entity)

    def add_relation(self, entity1, verb, entity2):
        if entity1 not in self.relations:
            self.relations[entity1] = {}
        if verb not in self.relations[entity1]:
            self.relations[entity1][verb] = set()
        self.relations[entity1][verb].add(entity2)

    def print_net(self):
        for entity1 in self.relations:
            for verb in self.relations[entity1]:
                for entity2 in self.relations[entity1][verb]:
                    print(f"{entity1} -- {verb} -- {entity2}")

def identify_entities_verbs(sentence):
    entities = set()
    verbs = []

    words = sentence.split()
    for word in words:
        if word.isalpha():
            entities.add(word)
        else:
            verbs.append(word.strip('.'))
    
    return entities, verbs

def main():
    semantic_net = SemanticNet()

    sentences = [
        "Jerry is a cat.",
        "Jerry was sitting on the sofa.",
        "Jerry is owned by Tom.",
        "Tom called Jerry.",
        "Jerry walked from the sofa to Tom.",
        "Tom gave some milk to Jerry.",
        "Jerry drank the milk."
    ]

    for sentence in sentences:
        entities, verbs = identify_entities_verbs(sentence)
        entities = list(entities)  
        for entity in entities:
            semantic_net.add_entity(entity)
        for verb in verbs:
            verb_parts = verb.split()
            if len(verb_parts) == 1:
                semantic_net.add_relation(entities[0], verb, entities[1])
            else:
                semantic_net.add_relation(entities[0], " ".join(verb_parts[:-1]), entities[1])

    semantic_net.print_net()

if __name__ == "__main__":
    main()

