# Sensitivity

[![arXiv](https://img.shields.io/badge/arXiv-2405.14686-b31b1b.svg)](https://arxiv.org/abs/2405.14686)

[**Efficient algorithms for the sensitivities of the Pearson correlation coefficient and its statistical significance to online data**](https://arxiv.org/abs/2405.14686)

## Requirements
To install the relevant dependencies, run
```setup
pip install -r requirements.txt
```
To build the main module, run
```setup
python setup.py build_ext --inplace
```

## Results

Experiment scripts are located in `experiments`.

### Synthetic Data 
To validate our algorithm on synthetic data randomly sampled from several distributions, run
```
python experiments/synthetic.py
```
to reproduce the exact figure in the main text. The experiment will be seeded.

### Real-world Stock Market Data 
To validate our algorithm on stock market data from the 2008 financial crisis, run
```
python experiments/stocks.py
```
to print the following results as obtained in the main text:

| Metric | Value   | Predicted Δ₁  | Brute-Force Δ₁ |
|--------|-------- |---------------|----------------|
| $r_n$  | 0.58028 | 1.15630       | 1.15630        |
| $p_n$  | 0.30502 | 0.69498       | 0.69491        |

**Table:** Predicted vs. Brute-Force Sensitivity Estimates

## Contributing

Our code is under an MIT license.
