"""cis-core — one pip install for the whole cis-* family.

Installing this package pulls in the three tools as dependencies, so a single
command gives you the complete Compliance-as-Code family:

    pip install cis-core
        -> cis-image   hardened golden image builder (console script: cis-image)
        -> cis-host    host hardening & drift automation (console script: cis-host)
        -> cis-cloud   multi-cloud CIS compliance (console script: cis-cloud)

The shared layer is reserved for content the family truly shares as it
consolidates:
- unified rule-catalog format (merging cis-cloud's catalog.json and
  cis-image's rules.json into one schema)
- shared report schema / export conventions (HTML / JSON / SARIF / XCCDF)
- family brand assets and naming conventions
"""

VERSION = "0.2.1"

__all__ = ["VERSION"]
