import sys
from pathlib import Path

# Allow importing from src/
sys.path.append(str(Path(__file__).resolve().parent.parent))

import streamlit as st
from src.app import summarize_text

# ── Page config ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="📝",
    layout="centered",
)

# ── Header ───────────────────────────────────────────────────────────────────
st.title("📝 AI Text Summarizer")
st.markdown("Powered by **OpenAI gpt-4o-mini**")
st.divider()

# ── Controls ─────────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    length = st.selectbox(
        "Summary length",
        options=["short", "medium", "long"],
        index=1,
    )

with col2:
    style = st.selectbox(
        "Output format",
        options=["paragraph", "bullet points", "one-liner"],
        index=0,
    )

# ── Input ────────────────────────────────────────────────────────────────────
text_input = st.text_area(
    "Paste your text here",
    height=250,
    placeholder="Enter the text you want to summarize...",
)

# ── Summarize button ─────────────────────────────────────────────────────────
if st.button("Summarize", type="primary", use_container_width=True):
    if not text_input.strip():
        st.warning("Please enter some text before summarizing.")
    else:
        with st.spinner("Generating summary..."):
            try:
                summary = summarize_text(text_input, length=length, style=style)
                st.divider()
                st.subheader("Summary")
                st.write(summary)

                # Word count comparison
                original_words = len(text_input.split())
                summary_words  = len(summary.split())
                reduction = round((1 - summary_words / original_words) * 100) if original_words else 0

                st.caption(
                    f"Original: **{original_words}** words → "
                    f"Summary: **{summary_words}** words  |  "
                    f"Reduced by **{reduction}%**"
                )
            except Exception as e:
                st.error(f"Error: {e}")
