# Inventory Reorder

Lead-time inventory thresholds with safety stock.

The reorder threshold is daily usage multiplied by lead days plus safety stock. Inventory exactly at the threshold triggers a warning.

## Run

Python 3.11 or newer; no external packages.

```sh
python main.py
python -m unittest discover -s tests -v
```

The module exposes its calculation as an importable function and includes a runnable example.
