# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_model.ipynb.

# %% auto 0
__all__ = ['random_SSM']

# %% ../nbs/01_model.ipynb 4
import numpy as np
import jax
import jax.numpy as jnp
import jax.numpy.linalg as jla
import equinox as eqx

from .modelArgs import ModelArgs

# %% ../nbs/01_model.ipynb 7
def random_SSM(rng, N):
    a_r, b_r, c_r = jax.random.split(rng, 3)
    A = jax.random.uniform(a_r, (N, N))
    B = jax.random.uniform(b_r, (N, 1))
    C = jax.random.uniform(c_r, (1, N))
    return A, B, C
