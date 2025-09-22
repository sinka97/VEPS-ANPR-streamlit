import streamlit as st

st.title("📘 About the endpoints")

st.write(
    "This application uses OpenAI models for Vehicle Information Extraction from images.\n"
    "Below is an overview of details for each implementation."
)

# --- Template for Models ---
def model_card(name, model_id, system_msg, user_msg, schema_example=None):
    with st.expander(f"🔹 {name}", expanded=False):
        st.markdown(f"**Model ID:** `{model_id}`")
        st.markdown("**System Message:**")
        st.code(system_msg, language="text")
        st.markdown("**User Message:**")
        st.code(user_msg, language="text")
        if schema_example:
            st.markdown("**Example JSON Schema Output:**")
            st.json(schema_example)

# --- Example Models ---
model_card(
    name="Version 1: gpt-4o simple extraction",
    model_id="gpt-4o",
    system_msg=(
        "You are a vision extraction assistant. Look at the image and extract:\n"
        "- Vehicle Plate Number\n- Vehicle Make\n- Vehicle Model\n- Vehicle Type\n- Vehicle Colour\n"
        "Return ONLY a JSON object that matches the provided schema. "
        "If something is unreadable, use an empty string."
    ),
    user_msg=(
        "Extract the following from the image: Vehicle Plate Number, "
        "Vehicle Make, Vehicle Model, Vehicle Type, Vehicle Colour. "
        "Output JSON only."
    ),
    schema_example={
        "Vehicle Plate Number": "SXX1234A",
        "Vehicle Make": "Toyota",
        "Vehicle Model": "Corolla",
        "Vehicle Type": "Sedan",
        "Vehicle Colour": "White",
    }
)

model_card(
    name="Version 2: gpt-4o-mini simple extraction",
    model_id="gpt-4o-mini",
    system_msg=(
        "You are a vision extraction assistant. Look at the image and extract:\n"
        "- Vehicle Plate Number\n- Vehicle Make\n- Vehicle Model\n- Vehicle Type\n- Vehicle Colour\n"
        "Return ONLY a JSON object that matches the provided schema. "
        "If something is unreadable, use an empty string."
    ),
    user_msg=(
        "Extract the following from the image: Vehicle Plate Number, "
        "Vehicle Make, Vehicle Model, Vehicle Type, Vehicle Colour. "
        "Output JSON only."
    ),
    schema_example={
        "Vehicle Plate Number": "SXX1234A",
        "Vehicle Make": "Toyota",
        "Vehicle Model": "Corolla",
        "Vehicle Type": "Sedan",
        "Vehicle Colour": "White",
    }
)

model_card(
    name="Version 3: gpt-4o multi extraction aggregator",
    model_id="gpt-4o",
    system_msg=(
        "x"
    ),
    user_msg=(
        "y"
    ),
    schema_example={
        "Vehicle Plate Number": "SXX1234A",
        "Vehicle Make": "Toyota",
        "Vehicle Model": "Corolla",
        "Vehicle Type": "Sedan",
        "Vehicle Colour": "White",
    }
)