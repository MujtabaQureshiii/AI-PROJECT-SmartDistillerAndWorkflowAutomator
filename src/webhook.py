"""
webhook.py — Sends extracted JSON to n8n webhook
"""
from datetime import datetime
from config import N8N_WEBHOOK_URL
import requests


def send_to_n8n(extracted_data: dict, targets: list) -> dict:
    payload = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "targets": targets,
        "data": extracted_data
    }
    return send_request(payload, targets)


def send_request(payload: dict, targets: list) -> dict:
    results = {}
    try:
        response = requests.post(
            N8N_WEBHOOK_URL,
            json=payload,
            timeout=10,
            headers={"Content-Type": "application/json"}
        )
        for target in targets:
            results[target] = {
                "status_code": response.status_code,
                "message": f"Data sent successfully to {target}." if response.status_code == 200
                           else f"Unexpected response: {response.text[:100]}"
            }
    except Exception as e:
        for target in targets:
            results[target] = {
                "status_code": 500,
                "message": f"Connection error: {str(e)}"
            }
    return results