# Wasserstein Sampling

Exploratory code for constructing sample sets that minimize Wasserstein distance to a target distribution, and comparing them against Monte Carlo, Latin Hypercube, and Halton sampling.

![Wasserstein vs others](wass-vs-others.png)

**Quickstart**
1. Create a virtual environment: `python -m venv .venv`
2. Activate it: `source .venv/bin/activate` (macOS/Linux) or `.\.venv\Scripts\activate` (Windows)
3. Install dependencies: `pip install -r requirements.txt`
4. Run the optimizer: `python wasserstein_sampling.py`

**Repository Layout**
- `wasserstein_sampling.py` Optimizes sample locations and writes `data-new.json`.
- `patcher.py` Generates comparison plots for Monte Carlo, Latin Hypercube, and Halton sampling.
- `areametric/` Area-metric utilities used by the notebooks.
- `*.ipynb` Research notebooks.
- `data.json` and `data-total.json` Saved sample sets used in plots.
- `fig/` Notebook output figures.
- `wass-vs-others.png` Reference plot shown above.

**Notes**
- `wasserstein_sampling.py` writes `data-new.json` in the repo root.
- `patcher.py` writes `wass-vs-mc.png` in the repo root.

**License**
GPL-3.0. See `LICENSE`.
