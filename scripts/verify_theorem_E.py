"""
verify_theorem_E.py — Verify Theorem E: a_p(A_r) = 0 when (2/p) = -1

For the curve A_r: y^2 = u(u+1)(u+r^2)(2u+(r-1)^2)(2u+(r+1)^2),
the Frobenius trace a_p = -sum_{u in F_p} (f(u)/p) where (./p) is
the Legendre symbol.

Theorem E claims a_p = 0 whenever (2/p) = -1.

This script verifies the claim by direct point counting over F_p
for all primes p < P_MAX with (2/p) = -1 and all r in [2, R_MAX].
"""

from sympy import isprime, legendre_symbol, primerange
import sys
import time

R_MAX = 100   # test r = 2, ..., R_MAX
P_MAX = 500   # test primes up to P_MAX


def f_eval(u, r, p):
    """Evaluate f(u) = u(u+1)(u+r^2)(2u+(r-1)^2)(2u+(r+1)^2) mod p."""
    val = u * (u + 1) * (u + r*r) * (2*u + (r-1)**2) * (2*u + (r+1)**2)
    return val % p


def frobenius_trace(r, p):
    """Compute a_p(A_r) = -sum_{u in F_p} (f(u)/p)."""
    s = 0
    for u in range(p):
        fu = f_eval(u, r, p)
        s += legendre_symbol(fu, p)
    return -s


def discriminant_zero(r, p):
    """Check if p divides the discriminant of f (i.e., roots collide mod p)."""
    # Roots: 0, -1, -r^2, -(r-1)^2/2, -(r+1)^2/2
    # We check if any pair of roots coincide mod p
    # This happens when p | r, p | (r-1), p | (r+1), p | (r^2-2r-1), p | (r^2+2r-1)
    if r % p == 0:
        return True
    if (r - 1) % p == 0:
        return True
    if (r + 1) % p == 0:
        return True
    if (r*r - 2*r - 1) % p == 0:
        return True
    if (r*r + 2*r - 1) % p == 0:
        return True
    # Also need 2 invertible (p != 2)
    if p == 2:
        return True
    return False


def main():
    print(f"Theorem E verification: r in [2, {R_MAX}], primes p < {P_MAX} with (2/p)=-1")
    print("=" * 70)

    total = 0
    fails = 0
    start = time.time()

    for r in range(2, R_MAX + 1):
        for p in primerange(5, P_MAX):
            # Skip bad primes
            if discriminant_zero(r, p):
                continue
            # Only test inert primes: (2/p) = -1
            if legendre_symbol(2, p) != -1:
                continue

            total += 1
            ap = frobenius_trace(r, p)

            if ap != 0:
                fails += 1
                print(f"  FAIL: r={r}, p={p}, a_p={ap}")

        # Progress report every 10 r values
        if r % 10 == 0:
            elapsed = time.time() - start
            print(f"  r={r} done ({total} tests so far, {elapsed:.1f}s)")

    elapsed = time.time() - start
    print("=" * 70)
    print(f"Total tests:  {total}")
    print(f"Failures:     {fails}")
    print(f"Time:         {elapsed:.1f}s")

    if fails == 0:
        print("\nTheorem E VERIFIED: a_p(A_r) = 0 for all tested (r, p) with (2/p) = -1.")
    else:
        print(f"\nWARNING: {fails} counterexample(s) found!")

    return fails


if __name__ == "__main__":
    sys.exit(main())
