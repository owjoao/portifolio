"""
Execute application of OriginKit Matrix and ADR-002 Dock on all remaining niches.
"""

import os, re
from remaining_niches_data import REMAINING_NICHES_DATA
from apply_originkit_and_docks import update_niche

print("Applying to remaining niches...")
count = 0
for n, d in REMAINING_NICHES_DATA.items():
    if update_niche(n, d):
        count += 1

print(f"Finished applying to {count}/{len(REMAINING_NICHES_DATA)} remaining niches!")

