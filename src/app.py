import psutil
from confluent_kafka import Producer
import json
import os

KAFKA_HOST = os.getenv("KAFKA_HOST")
KAFKA_TOPIC = os.getenv("KAFKA_TOPIC")

def sendToKafka(data):
    producer = Producer({"bootstrap.servers": KAFKA_HOST})
    producer.produce(KAFKA_TOPIC, value=json.dumps(data).encode("utf-8"))
    producer.flush()

def getCPUUsage():
    return psutil.cpu_percent(interval=1)

def main():
    try:
        cpu = getCPUUsage()
        data = {"cpu_usage": cpu}
        sendToKafka(data)
        print(f"CPU Usage: {cpu}%")
    except:
        print("Failed to get cpu usage.")

if __name__ == "__main__":
    main()