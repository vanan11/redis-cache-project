import time
from weather_api import get_weather

# First call - should be slow (2 seconds)
start = time.time()
result1 = get_weather("Jakarta")
time1 = time.time() - start
print(f"First call: {time1:.2f}s")
print(result1)

# Second call - should be fast (< 0.1 second)
start = time.time()
result2 = get_weather("Jakarta")
time2 = time.time() - start
print(f"Second call (cached): {time2:.2f}s")
print(result2)

# Third call after 5 minutes - should be slow again
# Tidak perlu menunggu 5 menit, cukup dijelaskan di laporan.