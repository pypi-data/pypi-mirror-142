# Description

A Python implementation of the nonparametric decomposition described in:

Norman-Haignere SV, Kanwisher NG, McDermott JH (2015). Distinct cortical pathways for music and speech revealed by hypothesis-free voxel decomposition. Neuron.

Also see [the repository for the original implementation.](https://github.com/snormanhaignere/nonparametric-ica). From the README there:

    The algorithm iteratively rotates the top K principal components of the data matrix, X, to maximize a measure of non-Gaussianity ('negentropy'). This procedure is closely related to standard algorithms for independent component analysis, but unlike standard algorithms does not depend on assumptions about the type of non-Gaussian distribution being identified. Because negentropy is estimated with a histogram, the algorithm tends to work well with a large number of data points (~10,000). The run-time of the algorithm increases substantially as the number of components is increased because the optimization is performed via a brute-force search over all pairs of components (run-time is thus proportional nchoosek(K,2) where K is the number of components).

# Usage

```python
import numpy as np

# Create synthetic data
M = 100 # number of features
N = 10000 # number of measures
K = 3 # number of components
R_true = np.random.rand(M,K)
W_true = np.random.exponential(scale = 1, size=(K,N))
X = R_true@W_true + .01*np.random.normal(M,N)

from npica import ICA
N_RANDOM_INITS = 10
RAND_SEED = 1
ica = ICA(K=K,N_RANDOM_INITS=N_RANDOM_INITS,RAND_SEED=RAND_SEED)
ica.fit(X)
print(ica.sources)
```