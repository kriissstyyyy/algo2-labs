import matplotlib.pyplot as plt
import networkx as nx
from lab7 import read_roads_csv, build_graph, edmonds_karp

ROADS_CSV = "/Users/hristinaskromuk/PyCharmMiscProject/roads.csv"


def get_flow_on_edges(filepath):
    farms, shops, edges = read_roads_csv(filepath)
    graph = build_graph(edges)

    super_source = "__SOURCE__"
    super_sink = "__SINK__"

    for farm in farms:
        graph[super_source][farm] = 10**9
        graph[farm][super_source] = 0
    for shop in shops:
        graph[shop][super_sink] = 10**9
        graph[super_sink][shop] = 0

    original = {u: dict(v) for u, v in graph.items()}

    max_flow = edmonds_karp(graph, super_source, super_sink)

    flow_on_edge = {}
    for u in original:
        for v, orig_cap in original[u].items():
            if u in (super_source, super_sink):
                continue
            if v in (super_source, super_sink):
                continue
            flow = orig_cap - graph[u][v]
            if flow > 0:
                flow_on_edge[(u, v)] = flow

    return farms, shops, edges, flow_on_edge, max_flow


def visualize(filepath):
    farms, shops, edges, flow_on_edge, max_flow = get_flow_on_edges(filepath)

    G = nx.DiGraph()

    for u, v, cap in edges:
        G.add_edge(u, v, capacity=cap)

    all_nodes = list(G.nodes())
    intersections = [n for n in all_nodes if n not in farms and n not in shops]

    pos = {}
    for i, f in enumerate(farms):
        pos[f] = (-2, i - len(farms) / 2)
    for i, x in enumerate(intersections):
        pos[x] = (0, i - len(intersections) / 2)
    for i, s in enumerate(shops):
        pos[s] = (2, i - len(shops) / 2)

    node_colors = []
    for node in G.nodes():
        if node in farms:
            node_colors.append("#4CAF50")
        elif node in shops:
            node_colors.append("#F44336")
        else:
            node_colors.append("#2196F3")

    edge_colors = []
    edge_widths = []
    for u, v in G.edges():
        if (u, v) in flow_on_edge:
            edge_colors.append("#FF9800")
            edge_widths.append(3)
        else:
            edge_colors.append("#999999")
            edge_widths.append(1)

    edge_labels = {}
    for u, v, data in G.edges(data=True):
        cap = data["capacity"]
        flow = flow_on_edge.get((u, v), 0)
        edge_labels[(u, v)] = f"{flow}/{cap}"

    plt.figure(figsize=(12, 7))
    plt.title(f"Максимальний потік: {max_flow} машин за день", fontsize=16, fontweight="bold")

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=1200)
    nx.draw_networkx_labels(G, pos, font_color="white", font_size=11, font_weight="bold")
    nx.draw_networkx_edges(G, pos, edge_color=edge_colors, width=edge_widths,
                           arrows=True, arrowsize=20, connectionstyle="arc3,rad=0.1")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

    legend_elements = [
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#4CAF50", markersize=12, label="Ферма"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#2196F3", markersize=12, label="Перехрестя"),
        plt.Line2D([0], [0], marker="o", color="w", markerfacecolor="#F44336", markersize=12, label="Магазин"),
        plt.Line2D([0], [0], color="#FF9800", linewidth=3, label="Активний потік"),
        plt.Line2D([0], [0], color="#999999", linewidth=1, label="Немає потоку"),
    ]
    plt.legend(handles=legend_elements, loc="upper left")
    plt.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    visualize(ROADS_CSV)
