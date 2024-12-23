from collections import defaultdict
from itertools import combinations
from pathlib import Path


def read_connections(input_path: Path) -> dict[str, set[str]]:
    connections = defaultdict(set)
    for line in input_path.read_text().splitlines():
        computer_a, computer_b = line.split("-")
        connections[computer_a].add(computer_b)
        connections[computer_b].add(computer_a)

    return connections


def find_largest_clique(connections: dict[str, set[str]]) -> set[str]:
    def bron_kerbosch(
        result: set[str],
        candidates: set[str],
        excluded: set[str],
    ) -> set[str]:
        if not candidates and not excluded:
            return result

        # Choose pivot that maximizes |candidates ∩ neighbors(pivot)|
        pivot = max(
            (len(candidates & connections[v]), v) for v in (candidates | excluded)
        )[1]

        max_clique = set()
        # Process vertices not connected to pivot
        for vertex in candidates - connections[pivot]:
            vertex_neighbors = connections[vertex]
            clique = bron_kerbosch(
                result | {vertex},
                candidates & vertex_neighbors,
                excluded & vertex_neighbors,
            )
            if len(clique) > len(max_clique):
                max_clique = clique
            candidates.remove(vertex)
            excluded.add(vertex)

        return max_clique

    return bron_kerbosch(set(), set(connections), set())


def solve_first(filename: str) -> int:
    input_path = Path(__file__).parent.parent / "in" / filename
    connections = read_connections(input_path)

    return sum(
        1
        for a, b, c in combinations(connections, 3)
        if (
            b in connections[a]
            and c in connections[a]
            and c in connections[b]
            and any(comp.startswith("t") for comp in (a, b, c))
        )
    )


def solve_second(filename: str) -> str:
    input_path = Path(__file__).parent.parent / "in" / filename
    lan_party_computers = find_largest_clique(read_connections(input_path))

    return ",".join(sorted(lan_party_computers))
