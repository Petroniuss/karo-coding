import json
import os
from pathlib import Path
import networkx as nx
from typing import List, Dict, Any

RouteSegment = Dict[str, Any]
AggregatedRoutes = List[List[RouteSegment]]

# helper function to read test files
def read_route_files(data_dir: str) -> AggregatedRoutes:
    data_path = Path(data_dir)
    
    all_routes: AggregatedRoutes = []
    files_processed = 0

    print(f"--- Starting Data Aggregation from '{data_dir}' ---")

    json_files = list(data_path.glob('*.json'))

    if not json_files:
        print(f"No JSON files found in the directory: {data_dir}")
        return all_routes

    for file_path in json_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

                if isinstance(data, list):
                    all_routes.append(data)
                    files_processed += 1
                    print(f"Successfully loaded data from: {file_path.name}")
                else:
                    print(f"Skipping file {file_path.name}: Expected a JSON list, but found a {type(data).__name__}.")

        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
        except json.JSONDecodeError:
            print(f"Error: Failed to decode JSON from file {file_path.name}. Check for syntax errors.")
        except Exception as e:
            print(f"An unexpected error occurred while reading {file_path.name}: {e}")

    print(f"--- Finished aggregation. {files_processed} files successfully processed. ---")
    return all_routes

def create_route_graph(aggregated_data: AggregatedRoutes) -> nx.Graph:
    # here you need to create nx graph based on AggregatedRoutes
    # TODO()
    raise Exception('get to work babe!')

# Here's how you can careate a simple graph.
def example_graph():
    G = nx.Graph()
    G.add_edge('A', 'B', weight=0.9)
    G.add_edge('B', 'C', weight=1.9) 
    print('-------- Example graph -----------------')
    print(G.edges)
    print(G.nodes)

    return G


if __name__ == "__main__":
    DATA_DIRECTORY = "data"

    # https://networkx.org/documentation/stable/reference/introduction.html
    routes_data = read_route_files(DATA_DIRECTORY)
    
    route_graph = example_graph()
    # route_graph = create_route_graph(routes_data)

    # ---------------------------------------------------------------------------------------
    print("\n--- Graph Summary ---")
    print(f"Nodes: {list(route_graph.nodes)}")
    print(f"Total Nodes (Stops): {route_graph.number_of_nodes()}")
    print(f"Total Edges (Connections): {route_graph.number_of_edges()}")
    
    # https://networkx.org/documentation/stable/reference/algorithms/shortest_paths/generated/networkx.algorithms.shortest_paths.generic.shortest_path_length.html#networkx.algorithms.shortest_paths.generic.shortest_path_length
    if route_graph.has_node('Kraków') and route_graph.has_node('Lipnica Mala'):
        # dist = 
        raise Exception('read documentation and call a correct function to get min distance')
        print(f"Edge A-B Weight (Distance): {dist}")