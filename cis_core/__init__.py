"""cis-core — shared foundation of the cis-* family.

This package is the shared layer planned for the cis-* family:

    cis-image  — hardened golden image builder
    cis-host   — host hardening & drift automation
    cis-cloud  — multi-cloud configuration compliance

Planned shared content (landing as the family consolidates its rule
catalogs and reporting):
- unified rule-catalog format (merging cis-cloud's catalog.json and
  cis-image's rules.json into one schema)
- shared report schema / export conventions (HTML / JSON / SARIF / XCCDF)
- family brand assets and naming conventions
"""

VERSION = "0.1.0"

__all__ = ["VERSION"]
