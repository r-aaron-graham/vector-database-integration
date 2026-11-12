# Vector Search Demo

Run an exact cosine similarity search over three synthetic vectors with Python.
The demo uses an in-memory fixture and the standard library.

```bash
python vector_demo.py
```

The first query ranks Cooling water first. The second ranks Power delivery
first. The ordering changes with the query vector. A zero vector, nonfinite
coordinate, or wrong dimension raises a clear error.

The three coordinates are illustrative features. The demo covers exact ranking
on a fixed set of vectors. A deployed index would add an embedding pipeline,
persistent storage, and retrieval evaluation.

[Compare retrieval strategies on a labeled dataset](https://github.com/r-aaron-graham/adaptive-rag-efficiency-lab)
