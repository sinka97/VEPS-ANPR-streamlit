import requests
import streamlit as st

# --------- Helper Functions ------------
def validate_openai_key(api_key: str) -> bool:
    url = "https://api.openai.com/v1/models"
    headers = {"Authorization": f"Bearer {api_key}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return True
    else:
        return False

# API Key Input
api_input = st.text_input(
    "Enter your OpenAI API Key:",
    type="password",
    value=st.session_state.get("api_key", ""),
    placeholder="sk-********************************",
)

# Save button
if st.button("Save API Key"):
    if api_input.strip():
        st.session_state.api_key = api_input.strip()
        if validate_openai_key(st.session_state.api_key):
            st.success("✅ API Key saved successfully!")
        else:
            st.warning("🚨 API Key is invalid!")
            st.session_state.api_key = ""
    else:
        st.error("⚠️ Please enter a valid API Key.")

# Show status if key is already saved
if st.session_state.get("api_key"):
    st.info("🔒 An API Key is currently stored. You can update it anytime.")