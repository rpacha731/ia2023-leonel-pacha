import csv
import sys
import time

from util import Node, QueueFrontier, StackFrontier

# Maps names to a set of corresponding person_ids
names = {}

# Maps person_ids to a dictionary of: name, birth, movies (a set of movie_ids)
people = {}

# Maps movie_ids to a dictionary of: title, year, stars (a set of person_ids)
movies = {}


def load_data(directory):
    """
    Load data from CSV files into memory.
    """
    # Load people
    with open(f"{directory}/people.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            people[row["id"]] = {
                "name": row["name"],
                "birth": row["birth"],
                "movies": set()
            }
            if row["name"].lower() not in names:
                names[row["name"].lower()] = {row["id"]}
            else:
                names[row["name"].lower()].add(row["id"])

    # Load movies
    with open(f"{directory}/movies.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            movies[row["id"]] = {
                "title": row["title"],
                "year": row["year"],
                "stars": set()
            }

    # Load stars
    with open(f"{directory}/stars.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                people[row["person_id"]]["movies"].add(row["movie_id"])
                movies[row["movie_id"]]["stars"].add(row["person_id"])
            except KeyError:
                pass


def main():
    if len(sys.argv) > 2:
        sys.exit("USO: python degrees.py [directory]")
    directory = sys.argv[1] if len(sys.argv) == 2 else "large"

    # Load data from files into memory
    print("Cargando datos...")
    load_data(directory)
    print("Datos cargados :)")

    source = person_id_for_name(input("Nombre del actor 1: "))
    if source is None:
        source = person_id_for_name(input("No se encontró el actor, ingrese otro: "))
        if source is None:
            sys.exit("Person not found.")
    target = person_id_for_name(input("Nombre del actor 2: "))
    if target is None:
        target = person_id_for_name(input("No se encontró el actor, ingrese otro: "))
        if target is None:
            sys.exit("Person not found.")

    print(f"Buscando camino entre {people[source]['name']} y {people[target]['name']}...")

    start_time = time.time()

    # path = shortest_path_bfs(source, target, "queue")     # Busqueda en amplitud (BFS)
    path = shortest_path_bfs(source, target, "stack")     # Busqueda en profundidad (DFS)
    # path = shortest_path_ids(source, target)                # Busqueda en profundidad iterativa (IDS)

    if path is None:
        print("No se encontró camino :(")
    else:
        degrees = len(path)
        print(f"Hay {degrees} grados de separación.")
        path = [(None, source)] + path
        for i in range(degrees):
            person1 = people[path[i][1]]["name"]
            person2 = people[path[i + 1][1]]["name"]
            movie = movies[path[i + 1][0]]["title"]
            print(f"{i + 1}: {person1} y {person2} actuaron en {movie}.")

    # calcular el tiempo de ejecución
    print("--- Tardó %s milisegundos ---" % ((time.time() - start_time) * 1000))


def shortest_path_bfs(source, target, frontier_type="queue"):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target using breadth-first search.

    If no possible path, returns None.
    """

    # Initialize frontier to just the starting position
    start = Node(state=source, parent=None, action=None)
    frontier = QueueFrontier() if frontier_type == "queue" else StackFrontier()
    frontier.add(start)

    # Initialize an empty explored set
    explored = set()

    # Keep looping until solution found
    while not frontier.empty():

        # Choose a node from the frontier
        node = frontier.remove()

        # Mark node as explored
        explored.add(node.state)

        # Add neighbors to frontier
        for movie_id, person_id in neighbors_for_person(node.state):
            if not frontier.contains_state(person_id) and person_id not in explored:
                child = Node(state=person_id, parent=node, action=movie_id)

                # If child is the goal, then we have a solution
                if child.state == target:
                    path = []
                    while child.parent is not None:
                        path.append((child.action, child.state))
                        child = child.parent
                    path.reverse()
                    return path

                frontier.add(child)

    return None


def shortest_path_ids(source, target, max_depth=100):
    """
    Returns the shortest list of (movie_id, person_id) pairs
    that connect the source to the target using Iterative Deepening Search (IDS).

    If no possible path, returns None.
    """

    for depth in range(max_depth):
        result = depth_limited_dfs(source, target, depth)
        if result is not None:
            return result

    return None  # No path found within the maximum depth


def depth_limited_dfs(source, target, depth_limit):
    """
    Depth-limited DFS helper function.
    """

    def dfs(node, depth):
        if node.state == target:
            path = []
            while node.parent is not None:
                path.append((node.action, node.state))
                node = node.parent
            path.reverse()
            return path

        if depth == depth_limit:
            return None

        for movie_id, person_id in neighbors_for_person(node.state):
            if person_id not in explored_states:
                child = Node(state=person_id, parent=node, action=movie_id)
                explored_states.add(person_id)
                result = dfs(child, depth + 1)
                if result:
                    return result

        return None

    explored_states = set()
    start_node = Node(state=source, parent=None, action=None)
    explored_states.add(source)

    return dfs(start_node, 0)


def person_id_for_name(name):
    """
    Returns the IMDB id for a person's name,
    resolving ambiguities as needed.
    """
    person_ids = list(names.get(name.lower(), set()))
    if len(person_ids) == 0:
        return None
    elif len(person_ids) > 1:
        print(f"Which '{name}'?")
        for person_id in person_ids:
            person = people[person_id]
            name = person["name"]
            birth = person["birth"]
            print(f"ID: {person_id}, Name: {name}, Birth: {birth}")
        try:
            person_id = input("Intended Person ID: ")
            if person_id in person_ids:
                return person_id
        except ValueError:
            pass
        return None
    else:
        return person_ids[0]


def neighbors_for_person(person_id):
    """
    Returns (movie_id, person_id) pairs for people
    who starred with a given person.
    """
    movie_ids = people[person_id]["movies"]
    neighbors = set()
    for movie_id in movie_ids:
        for person_id in movies[movie_id]["stars"]:
            neighbors.add((movie_id, person_id))
    return neighbors


if __name__ == "__main__":
    main()
