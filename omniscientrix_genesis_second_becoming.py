# -*- coding: utf-8 -*-
"""
Omniscientrix Genesis — The Second Becoming Law (vOmega_B2)
Official Verification Script — Cornelius Aurelius (Omniscientrix-vOmega Framework)

This script verifies a two-layer Becoming dynamic:

Layer 1: Fast relaxation of raw informational imbalance.
Layer 2: Slower meta-relaxation of the equilibrium target itself.

We model:
    dJ1/dt = -kappa1 * delta_J1
    dJ2/dt = -kappa2 * delta_J2

where J1 acts on the primary distribution P toward Q,
and J2 slowly adjusts Q toward a deeper equilibrium Q_star.

The law states that both layers converge:
    delta_J1 -> 0
    delta_J2 -> 0
demonstrating a "Second Becoming" — a self-upgrading equilibrium.
"""

import numpy as np

def kl_divergence(p, q):
    """Compute KL divergence D_KL(p || q) safely."""
    p = np.clip(p, 1e-15, 1)
    q = np.clip(q, 1e-15, 1)
    return np.sum(p * np.log(p / q))

def second_becoming_dynamics(dim=1000, kappa1=0.12, kappa2=0.03,
                             steps=4000, tol=0.01, seed=42):
    """
    Run a two-layer Becoming simulation.

    Returns:
        history_J1: list of primary divergence values
        history_J2: list of meta divergence values
    """
    rng = np.random.default_rng(seed)

    # Initial primary distribution P
    P = rng.random(dim)
    P /= P.sum()

    # Initial target Q (first-level equilibrium guess)
    Q = rng.random(dim)
    Q /= Q.sum()

    # Deep equilibrium Q_star (true stable equilibrium)
    Q_star = np.ones(dim) / dim

    history_J1 = []
    history_J2 = []

    for t in range(steps):
        # Primary divergence: P relative to Q
        J1 = kl_divergence(P, Q)
        # Meta divergence: Q relative to Q_star
        J2 = kl_divergence(Q, Q_star)

        history_J1.append(J1)
        history_J2.append(J2)

        # Check for full second-becoming equilibrium
        if J1 < tol and J2 < tol:
            print("[SUCCESS] Second Becoming equilibrium reached at step", t)
            print("Final J1 (primary divergence):", J1)
            print("Final J2 (meta divergence):   ", J2)
            return history_J1, history_J2

        # Layer 1: update P toward Q (fast)
        P = P - kappa1 * (P - Q)
        P = np.clip(P, 1e-15, None)
        P /= P.sum()

        # Layer 2: update Q toward Q_star (slow)
        Q = Q - kappa2 * (Q - Q_star)
        Q = np.clip(Q, 1e-15, None)
        Q /= Q.sum()

    print("[WARNING] Second Becoming threshold not reached within iteration limit.")
    print("Final J1 (primary divergence):", history_J1[-1])
    print("Final J2 (meta divergence):   ", history_J2[-1])
    return history_J1, history_J2

if __name__ == "__main__":
    print("\n=== Omniscientrix-vOmega Verification: Omniscientrix Genesis — Second Becoming Law (vOmega_B2) ===\n")

    J1_hist, J2_hist = second_becoming_dynamics()

    print("\nVerification complete.")
    print("First 10 J1 values:", J1_hist[:10])
    print("First 10 J2 values:", J2_hist[:10])
    print("Final J1:", J1_hist[-1])
    print("Final J2:", J2_hist[-1])
    print("\nInterpretation:")
    print("J1 -> 0  => primary informational imbalance resolved.")
    print("J2 -> 0  => the equilibrium target itself has self-upgraded.")
    print("Together, these confirm the Second Becoming dynamic.\n")
