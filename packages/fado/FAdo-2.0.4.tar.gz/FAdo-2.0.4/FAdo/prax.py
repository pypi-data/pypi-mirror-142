# -*- coding: utf-8 -*-
"""**Polynomial Random Approximation Algorithms**

.. *Authors:* Rogério Reis & Nelma Moreira

.. *This is part of FAdo project*   https://fado.dcc.fc.up.pt.

.. *Copyright:* 1999-2022 Rogério Reis & Nelma Moreira {rvr,nam}@dcc.fc.up.pt

.. *Contributions by:*
   - Stavros Konstantinidis
   - Mitja Mastnak

.. This program is free software; you can redistribute it and/or
   modify it under the terms of the GNU General Public License as published
   by the Free Software Foundation; either version 2 of the License, or
   (at your COption) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
   or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
   for more details.

   You should have received a copy of the GNU General Public License along
   with this program; if not, write to the Free Software Foundation, Inc.,
   675 Mass Ave, Cambridge, MA 02139, USA."""
from . common import *
from . codes import *
from random import random, randint
from math import ceil


def minI(a, t, u=None):
    """ An operator that returns a t-independent language containing L(a)

    Args:
        a (FA): the initial automaton
        t (Transducer): input-altering transducer
        u (FA | None): universe to consider
    Returns:
        NFA: """
    tinv = t.inverse()
    tt = t | tinv
    if u is None:
        b = ~(tt.runOnNFA(a)).trim()
    else:
        b = (u & ~ (tt.runOnNFA(a))).trim()
    return (b & ~(tinv.runOnNFA(b))).trim()

def unive_index(g, aut, prop):
    """Universality index of a automaton for a given distribution

    Args:
        g (GenWordDis): distribution
        aut (FA): automaton
    Returns:
        float: universality index"""
    n, m = prax_parameters(g)
    pos = 0.0
    b = prop.Aut.runOnNFA(aut) | prop.Aut.inverse().runOnNFA(aut) | aut
    for _i in range(n):
        w = next(g)
        if b.evalWordP(w):
            pos += 1
    return pos/n

def prax_parameters(g):
    """Prax parameters for a given experiment"""
    return (g.n_tries, g.max_length)


def prax_univ_nfa(g, a, debug=False):
    """Polynomial Randomized Approximation (PRAX) to NFA universality

    Args:
        a (FA): the automaton being tested
        e (float): admissible error
        prob_func: probability function
        alpha (set): alphabet of the language
    Returns:
        bool:

    .. seealso::
        S.Konstantinidis, M.Mastnak, N.Moreira, R.Reis. Approximate NFA Universality and Related Problems Motivated
        by Information Theory, arXiv, 2022.

    .. versionadded:: 2.0.4"""
    n,m = prax_parameters(g)
    for _i in range(n):
        w = next(g)
        if not a.evalWordP(w):
            if debug:
                print("couterexample of size-> ",len(w), end = " ")
            return False
    return True


def f_dirichlet(n, d=1, t=2.000001):
    """Dirichlet distribution function

    Args:
        n (int): evaluation point
        d (int | float): displacement
        t (int | float):
    Returns:
        float:

    .. versionadded:: 2.0.4"""
    if n >= d:
        return 1/zeta(t) * ((n + 1 - d) ** (-t))
    else:
        return 0


def f_laplace(n, d=1, z=0.99):
    """Laplace distribution function

    Args:
         n (int): evaluation point
         d (int): displacement
         z (float): a number 9<z<1
    Returns:
         float:

    Raises:
        FAdoGeneralError: if z is null"""
    if z == 0.0:
        raise FAdoGeneralError("Value of z cannot be null")
    z = 1/z
    if n < d:
        return 0.0
    else:
        return (1-z) * z ** (n-d)


class GenWordDis(object):
    """Word generator according to a given distribution funtion (used for sizes), for prax test

    :ivar list sigma: alphabet
    :ivar function pf: distribution function
    :ivar float e: acceptable error
    :ivar int n_tries: size of the sample
    :ivar int max_length: maximal size of the words sampled
    :ivar list dist: comulative probability for each size consedered (up to max_lengtg)"""
    def __init__(self, f, alf, e):
        self.sigma = list(alf)
        self.pf = f
        e1 = min(e, 1/6)
        self.e = e1
        self.n_tries = ceil(5 / (e1 - 5 * e1 ** 2) ** 2)
        s, i = 0, 1
        while s + e1 * e1 < 1:
            s += self.pf(i)
            i += 1
        self.max_length = i - 1
        foo = 0
        self.dist = []
        for i in range(1, self.max_length + 1):
            bar = f(i)
            self.dist.append(foo + bar)
            foo += bar


    def __iter__(self):
        return self

    def __next__(self):
        r = random()
        sz = self._find(r, 0, len(self.dist) - 1)
        k = len(self.sigma)
        return Word([self.sigma[randint(0, k - 1)] for _ in range(sz)])

    def _find(self, r, mi, ma):
        if mi == ma:
            return mi+1
        elif ma-mi == 1:
            if r <= self.dist[mi]:
                return mi+1
            else:
                return ma+1
        else:
            i = (ma - mi) // 2
            if r <= self.dist[mi + i]:
                return self._find(r, mi, mi + i)
            else:
                return self._find(r, mi + i, ma)
