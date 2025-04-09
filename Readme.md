# bioLOLPython

> analyze DNA in lolspeak

## 🐱 What is LOLCODE?

LOLOLOL okay so listen up Gen Z 😹 — before TikTok memes and Discord kittens, there was a meme format called **lolcats**. These were internet-famous cat pictures with broken-English captions called **lolspeak** (or **catspeak**). Think:
  
- “I CAN HAS CHEEZBURGER?”
- “Y U NO FETCH?”
- “I’M IN UR CODE, BREAKIN UR LOOPZ”

From this glorious chaos, **LOLCODE** was born in 2007 by Adam Lindsay. It’s a programming language styled entirely in lolspeak. It’s not meant for serious production use — it’s a meme, a parody, and a challenge all in one.

Popular LOLcats included **Grumpy Cat**, **Longcat**, and **Serious Cat**, and this language was their honorary coding tongue.

**LOLPython** was later developed by Andrew Dalke as a LOLCODE-inspired interpreter that transpiles to Python. That’s what this project builds on — but with extra chromosomes: we’ve added **bioinformatics**.

Welcome to **bioLOLPython** — a meme-powered biological scripting language for coding with chaos and DNA 🧬.

try it at [https://bioLOL.streamlit.app](https://bioLOL.streamlit.app)

## 🤖 bioLOLPython Extension

This is a **meme-inspired biological scripting environment** built on top of the original LOLPython interpreter.  
Vibe coded (sorry not sorry) by **Chen Hsieh (2025)**, it updates LOLPython to Python 3 and adds support for biological sequence analysis using Biopython.

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
