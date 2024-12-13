import json
import random

import requests


def search_product(image_path: str) -> list:
    url = "https://search-by-photo.wb.ru/uploadsearch"
    files = [
        ('image', (image_path, open(image_path, 'rb'), 'image/jpeg'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, files=files)

    if response.status_code == 200:
        data = json.loads(response.text)
        if data.get("status") == "OK" and data.get("result"):
            results = data["result"]
            random_selections = []

            # Group results
            for i in range(0, len(results), 8):
                group = results[i:i + 8]
                if group:
                    random_item = random.choice(group)
                    random_selections.append(random_item["im_name"])

            sorted_selections = sorted(random_selections)

            # Top
            top_10 = sorted_selections[:10]
            return top_10
        else:
            raise ValueError("Response data error")
    else:
        raise ConnectionError(f"HTTP Error: {response.status_code}")
