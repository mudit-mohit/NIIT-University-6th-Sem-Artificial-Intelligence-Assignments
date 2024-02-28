import networkx as nx
import matplotlib.pyplot as plt

class Variable:
    def __init__(self, name, domain):
        self.name = name
        self.domain = domain

class ConstraintGraph:
    def __init__(self):
        self.variables = {}
        self.binary_constraints = []

    def add_variable(self, name, domain):
        self.variables[name] = Variable(name, domain)

    def add_unary_constraint(self, var_name, operator, constant):
        variable = self.variables[var_name]
        if operator == '<':
            variable.domain = [val for val in variable.domain if val < constant]
        # Add handling for other operators if needed

    def add_binary_constraint(self, var1_name, operator, var2_name, arithmetic_operator, constant):
        self.binary_constraints.append((var1_name, operator, var2_name, arithmetic_operator, constant))

    def apply_binary_constraints(self):
        for constraint in self.binary_constraints:
            var1_name, operator, var2_name, arithmetic_operator, constant = constraint
            var1 = self.variables[var1_name]
            var2 = self.variables[var2_name]

            # Implement logic to adjust domains based on binary constraints
            if arithmetic_operator == '+':
                var2.domain = [val - constant for val in var2.domain if val - constant in var1.domain]
            elif arithmetic_operator == '-':
                var2.domain = [val + constant for val in var2.domain if val + constant in var1.domain]
            # Add handling for other arithmetic operators if needed

    def draw_constraint_graph(self):
        G = nx.Graph()

        for var_name, variable in self.variables.items():
            G.add_node(var_name, domain=variable.domain)

        for constraint in self.binary_constraints:
            var1_name, _, var2_name, _, _ = constraint
            G.add_edge(var1_name, var2_name)

        pos = nx.spring_layout(G)
        labels = {node: f"{node}\nDomain: {self.variables[node].domain}" for node in G.nodes}

        nx.draw(G, pos, with_labels=True, labels=labels, font_weight='bold', node_color='skyblue')
        plt.show()

# Example usage
graph = ConstraintGraph()

# Add variables
graph.add_variable('A', [1, 2, 3])
graph.add_variable('B', [1, 2, 3])
# Add unary constraints
graph.add_unary_constraint('A', '<', 5)
# Add binary constraints
graph.add_binary_constraint('A', '>', 'B', '+', 1)

# Draw initial constraint graph
graph.draw_constraint_graph()

# Apply binary constraints and adjust domains
graph.apply_binary_constraints()

# Draw constraint graph with adjusted domains
graph.draw_constraint_graph()
