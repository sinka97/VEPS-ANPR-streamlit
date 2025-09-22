import json
import streamlit as st
from openai import OpenAI
from typing import Dict
from utils.common import to_data_url, sanitize_response

def extract_info_v1(file, client: OpenAI) -> Dict:
    MODEL_V1 = "gpt-4o"
    SCHEMA_V1 = {
        "name": "VehicleInfo",
        "strict": True,
        "schema": {
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "Vehicle Plate Number": {"type": "string"},
                "Vehicle Make": {"type": "string"},
                "Vehicle Model": {"type": "string"},
                "Vehicle Type": {"type": "string"},
                "Vehicle Colour": {"type": "string"},
            },
            "required": [
                "Vehicle Plate Number",
                "Vehicle Make",
                "Vehicle Model",
                "Vehicle Type",
                "Vehicle Colour",
            ],
        },
    }

    SYSTEM_V1 = (
        "You are a vision extraction assistant. Look at the image and extract:\n"
        "- Vehicle Plate Number\n- Vehicle Make\n- Vehicle Model\n- Vehicle Type\n- Vehicle Colour\n"
        "Return ONLY a JSON object that matches the provided schema. "
        "If something is unreadable, use an empty string."
    )

    USER_V1 = (
        "Extract the following from the image: Vehicle Plate Number, Vehicle Make, "
        "Vehicle Model, Vehicle Type, Vehicle Colour. Output JSON only."
    )

    data_url = to_data_url(file)

    resp = client.chat.completions.create(
        model=MODEL_V1,
        response_format={"type": "json_schema", "json_schema": SCHEMA_V1},
        messages=[
            {"role": "system", "content": SYSTEM_V1},
            {"role": "user", "content": [
                {"type": "text", "text": USER_V1},
                {"type": "image_url", "image_url": {"url": data_url}},
            ]},
        ],
    )

    result: Dict = json.loads(resp.choices[0].message.content)
    return sanitize_response(result)
