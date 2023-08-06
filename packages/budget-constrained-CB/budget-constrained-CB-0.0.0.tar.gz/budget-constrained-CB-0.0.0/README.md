# Budget Contextual Bandits

Constrained Contextual Bandits for Personalized Recommendation. Adding budget constraints to a few popular MAB/CB methods:

- Context-Free Epsilon Greedy
- LinUCB [[1]](#1)
- UCB-ALP [[2]](#2)
- HATCH [[3]](#3)

## Development

### Prerequisites

- make
- node (required for pyright. Install via `brew install node`)
- python >= 3.7

### Getting started

To get started run `make install`. This will:

- install git hooks for formatting & linting on git push
- create the virtualenv in _.venv/_
- install this package in editable mode

Then run `make` to see the options for running checks, tests etc.

`. .venv/bin/activate` activates the virtualenv. When the requirements in `setup.py` change, the virtualenv is updated by the make targets that use the virtualenv.

### Benchmark different methods against random and greedy policy

Check out the [notebook](https://github.com/HongleiXie/budgetCB/blob/master/example_data/example.ipynb) to see the comparison among a variety of methods including `UCB-ALP`, `LinUCB` and `HATCH`, against the two baseline policies `Random` and `Greedy`.

Rolling mean of rewards v.s. number of rounds:

![pic](./output.png)

### Reference

<a id="1">[1]</a>
Li, Lihong, et al. "A contextual-bandit approach to personalized news article recommendation." *Proceedings of the 19th international conference on World wide web.* 2010.

<a id="2">[2]</a>
Wu, Huasen, et al. "Algorithms with logarithmic or sublinear regret for constrained contextual bandits." *Advances in Neural Information Processing Systems.* 2015.

<a id="3">[3]</a>
Yang, Mengyue, et al. "Hierarchical Adaptive Contextual Bandits for Resource Constraint based Recommendation." *Proceedings of The Web Conference 2020.* 2020.
