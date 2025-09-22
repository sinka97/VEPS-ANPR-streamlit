from base64 import b64encode
from typing import Dict

def to_data_url(file) -> str:
    """Convert uploaded file to data URL for OpenAI image input."""
    encoded = b64encode(file.read()).decode("utf-8")
    return f"data:image/jpeg;base64,{encoded}"

def sanitize_response(result: Dict) -> Dict:
    """Ensure all required keys exist, even if empty."""
    for key in ["Vehicle Plate Number", "Vehicle Make", "Vehicle Model", "Vehicle Type", "Vehicle Colour"]:
        if key not in result:
            result[key] = ""
    return result