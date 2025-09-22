import json
import streamlit as st
from openai import OpenAI
from typing import Dict
from utils import v1_simple_4o, v2_simple_4o_mini

# ---------------- Selector Mapping ----------------
EXTRACTION_FUNCS = {
    "V1 - gpt-4o": v1_simple_4o.extract_info_v1,
    "V2 - gpt-4o-mini": v2_simple_4o_mini.extract_info_v2,
    # add more versions here...
}

# ---------------- Streamlit UI ----------------
st.set_page_config(page_title="Vehicle Info Extractor", layout="centered")
st.title("Vehicle Information Extraction")

if "api_key" not in st.session_state:
    st.warning("⚠️ Please enter your OpenAI API Key in the Config Page to continue.")
    st.page_link("pages/Config.py", label="Click here to go to Config", icon="⚙️")
else:
    client = OpenAI(api_key=st.session_state.api_key)

    version = st.selectbox("Choose extraction endpoint:", list(EXTRACTION_FUNCS.keys()))

    uploaded_file = st.file_uploader("Upload a vehicle image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

        if st.button("Extract Information"):
            with st.spinner("Extracting details..."):
                try:
                    uploaded_file.seek(0)  # reset pointer
                    extract_info = EXTRACTION_FUNCS[version]
                    result = extract_info(uploaded_file, client)
                    st.success("Extraction complete!")
                    st.json(result)
                except Exception as e:
                    st.error(f"Error: {e}")
