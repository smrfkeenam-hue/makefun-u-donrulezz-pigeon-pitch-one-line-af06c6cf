import os

# One-line elevator pitch: a city pigeon pitches investors on Crumbly, a
# breadcrumb subscription box. The joke is the seed round — literal seed.
ENTRY = "Crumbly: a breadcrumb subscription box, delivered by pigeon and eaten by pigeon — we're raising a seed round, and yes, the seed is literal."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
with open(output_dir + "/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY)
