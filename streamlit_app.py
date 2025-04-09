import streamlit as st
from bioLOLPython.interpreter import *
import tempfile
import io
from contextlib import redirect_stdout

# Styling
st.set_page_config(page_title="bioLOL Webshell", layout="centered")
st.markdown(f"""
    <style>
        .stApp {{
            background-image: url('static/bg_lolcat.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            color: #33ff33;
            font-family: 'Courier New', Courier, monospace;
        }}
        .stTextArea textarea {{
            background-color: rgba(0,0,0,0.7) !important;
            color: #33ff33 !important;
        }}
        .stButton>button {{
            background-color: #111;
            border: 1px solid #33ff33;
            color: #33ff33;
        }}
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        body {
            background-color: #0f0f0f;
            color: #33ff33;
            font-family: 'Courier New', Courier, monospace;
        }
        .stTextArea textarea {
            background-color: #111111 !important;
            color: #33ff33 !important;
        }
        .stButton>button {
            color: #33ff33;
            background-color: #222222;
            border: 1px solid #33ff33;
        }
    </style>
""", unsafe_allow_html=True)

st.title("😹 bioLOL Interpurr-ter")
st.markdown("_Cuz sometimes your genes just need more memes._")

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
