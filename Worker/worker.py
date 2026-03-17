import time
import redis

r = redis.Redis(host="redis", port=6379)

while True:
    try:
        data = r.get("counter")
        print("Counter value:", data)
    except Exception as e:
        print("Error:", e)
    
    time.sleep(5)