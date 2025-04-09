import streamlit as st
from bioLOLPython.interpreter import *
import tempfile
import io
from contextlib import redirect_stdout

# Styling
st.set_page_config(
    page_title="bioLOL Webshell", 
    layout="centered",
    page_icon="😹"
)
st.markdown(
    """
    <style>
        .stApp {
            background: url('') repeat;
            color: #33ff33;
            font-family: 'Courier New', Courier, monospace;
        }
        .stTextArea textarea {
            background-color: rgba(0,0,0,0.7) !important;
            color: #33ff33 !important;
        }
        .stButton>button {
            background-color: #111;
            border: 1px solid #33ff33;
            color: #33ff33;
        }
    </style>
""", unsafe_allow_html=True)


st.title("😹 bioLOL Interpurr-ter")
st.markdown("_Cuz sometimes your genes just need more memes._")

col1, col2 = st.columns(2)
with col1:
    st.markdown("""

### 🐱 What is Lolspeak?

Lolspeak is the internet dialect of the classic **lolcat** meme era — think early 2000s cat pictures with broken English like:
- "I CAN HAS CHEEZBURGER?"
- "I'M IN UR BASE, SEQUENCIN UR DNA"
                
here is an example of lolspeak generated by ChatGPT-4o:


![](https://github.com/ChenHsieh/bioLOLPython/blob/master/static/bg_lolcat.jpg?raw=true)

**LOLCODE** was invented as a joke programming language using lolspeak. This app builds on that glorious nonsense — adding bioinformatics commands so you can meme your way through molecular biology 🧬😹

---
### 💻 How to Use

- Pick an example from the dropdown (like GC content, translation, alignment), or write your own in lolspeak-style scripting.
- Click **"RUN da CODE"** to see the output.
- Try commands like `DNA GO X ITZ "ATGC"`, `GC BOMB X`, `TRANSLATE`, `I CRAVE VIOLENCE`, etc.

Make it chaotic. Make it bio. Make it LOL.
    """)
with col2:
    # Examples
    examples = {
        "GC Content": """HAI GENZOME 1.0
    DNA GO X ITZ "ATGCATGC"
    GC BOMB X
    KTHXBYE""",
        "Protein Translation": """HAI GENZOME 1.0
    DNA GO Y ITZ "ATGGAGGAGCC"
    TRANSLATE Y
    VISIBLE "🧬 Protein: " + Y
    KTHXBYE""",
        "Alignment": """HAI GENZOME 1.0
    DNA GO A ITZ "ATGCGTAGG"
    DNA GO B ITZ "ATGCGTACG"
    ALIGN A WIT B
    KTHXBYE"""
    }

    # Selection
    script_option = st.selectbox("💾 Choose an example or start typing your own:", ["(Write your own)"] + list(examples.keys()))

    # Script input
    default_code = examples.get(script_option, "HAI GENZOME 1.0\nDNA GO X ITZ \"ATGC\"\nVISIBLE X\nKTHXBYE")
    code = st.text_area("✏️ Write your .lolz code here:", default_code, height=200)

    # Run
    if st.button("💥 RUN da CODE"):
        st.subheader("🖨️ Outputz")
        output_buffer = io.StringIO()
        with redirect_stdout(output_buffer):
            try:
                for line in code.splitlines():
                    result = handle_line(line.strip())
                    if result is not None:
                        print(result)
            except Exception as e:
                st.error(f"Oopsie: {e}")
        st.code(output_buffer.getvalue(), language="text")
