import time
import json
import redis

# Koneksi ke Redis
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    db=0,
    decode_responses=True
)

def get_weather(city):
    """Simulasi API call yang lambat dengan Redis caching"""

    cache_key = f"weather:{city.lower()}"

    cached_data = redis_client.get(cache_key)

    if cached_data:
        print("Data diambil dari cache")
        return json.loads(cached_data)

    print("Data diambil dari API")
    time.sleep(2)

    data = {
        "city": city,
        "temperature": "30°C",
        "condition": "Cloudy"
    }

    # 3. Simpan ke Redis
    redis_client.set(cache_key, json.dumps(data))

    # 4. Set expiry 5 menit
    redis_client.expire(cache_key, 300)

    return data