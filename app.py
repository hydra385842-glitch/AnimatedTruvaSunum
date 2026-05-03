import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path

st.set_page_config(page_title="Truva Savaşı", page_icon="⚔️", layout="wide", initial_sidebar_state="collapsed")

st.markdown("<style>#MainMenu,footer,header{visibility:hidden;}.block-container{padding:0!important;max-width:100%!important;}iframe{border:none!important;}</style>", unsafe_allow_html=True)

html_content = (Path(__file__).parent / "truva.html").read_text(encoding="utf-8")
components.html(html_content, height=900, scrolling=False)
