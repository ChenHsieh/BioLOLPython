# bioLOLPython

## 🤖 bioLOLPython Extension

This is a **meme-inspired biological scripting environment** built on top of the original LOLPython interpreter.  
Vibe coded by **Chen Hsieh (2025)**, it updates LOLPython to Python 3 and adds support for biological sequence analysis using Biopython.

### ✨ Added Features
- ✅ `DNA GO <name> ITZ "SEQ"` — declare a DNA sequence
- 🔁 `REVERSE THAT <name>` — reverse complement
- 🔬 `GC BOMB <name>` — calculate GC content
- 💧 `TRANSCRIBE <name>` — DNA → RNA
- 🍖 `TRANSLATE <name>` — DNA → Protein
- 💣 `I CRAVE VIOLENCE <name>` — introduce random mutation
- 🤝 `ALIGN A WIT B` — global alignment (with meme-style scoring)
- 👁️ `VISIBLE "..." + <name>` — print sequence variables in messages

### 🚀 Example

```
HAI GENZOME 1.0

DNA GO X ITZ "ATGCGTAC"
GC BOMB X
TRANSLATE X
VISIBLE "💥 new protein: " + X

KTHXBYE
```

### 🔬 Installation

You can install bioLOLPython globally using [`pipx`](https://pypa.github.io/pipx/):

```
pipx install git+https://github.com/ChenHsieh/bioLOLPython.git
```

Or install locally with pip for development:

```
git clone https://github.com/ChenHsieh/bioLOLPython.git
cd bioLOLPython
pip install -e .
```

✅ After installation, you can run `.lolz` scripts like this:

```
bioLOL path/to/script.lolz
```

> Requires Python ≥ 3.8 and the dependencies `biopython` and `ply`
