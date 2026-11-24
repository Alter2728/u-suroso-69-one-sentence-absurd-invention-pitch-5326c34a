"""One-Sentence Absurd Invention Pitch — a TV remote that ends arguments
by hiding until everyone agrees on a documentary nobody wanted."""

import os

# Revised pitch (v2): "begins" -> "breaks out" for a punchier trigger, and the
# vague "a documentary nobody wanted" -> the concrete, funnier detail of a
# nature documentary about moss, which is the kind of thing nobody picks
# on purpose — the remote only returns once the argument has been settled
# by mutual boredom.
SENTENCE = (
    "A TV remote that hides itself the moment an argument about what to watch "
    "breaks out, then comes back only after everyone has agreed on a nature "
    "documentary about moss."
)

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(SENTENCE)
