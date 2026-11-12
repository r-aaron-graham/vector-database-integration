"""Run exact cosine similarity over a small in-memory fixture."""

from math import hypot, isfinite


VECTORS = (
    ("Cooling water", (1.0, 0.1, 0.0)),
    ("Power delivery", (0.1, 1.0, 0.0)),
    ("Network routing", (0.0, 0.1, 1.0)),
)


def perform_similarity_search(query_vector):
    query = tuple(query_vector)
    if len(query) != len(VECTORS[0][1]) or not all(map(isfinite, query)):
        raise ValueError("Expected three finite query coordinates")
    scale = max(map(abs, query))
    if scale == 0:
        raise ValueError("Expected a nonzero query vector")
    scaled_query = tuple(value / scale for value in query)
    norm = hypot(*scaled_query)
    unit_query = tuple(value / norm for value in scaled_query)

    def similarity(entry):
        _, vector = entry
        return sum(a * b for a, b in zip(unit_query, vector)) / hypot(*vector)

    return [label for label, _ in sorted(VECTORS, key=similarity, reverse=True)]


if __name__ == "__main__":
    for query in ([1, 0, 0], [0, 1, 0]):
        print(f"{query} → {perform_similarity_search(query)}")
