import threading
import time
import random
from datetime import datetime
import queue
import mysql.connector

# MySQL 연결 설정 (사용자 환경에 맞게 수정 필요)
DB_CONFIG = {
    "host": "localhost",
    "user": "your_mysql_user", 
    "password": "your_mysql_password",
    "database": "smart_farm_db" # 미리 생성해야 함
}

# 1. ParmSensor 클래스 정의
class ParmSensor:
    def __init__(self, name):
        self.name = name
        self.temperature = None
        self.illuminance = None
        self.humidity = None
        self.lock = threading.Lock() # 쓰레드 안전을 위한 락

    def SetData(self):
        # 주어진 범위 내에서 랜덤 값 생성
        with self.lock:
            self.temperature = random.randint(20, 30)
            self.illuminance = random.randint(5000, 10000)
            self.humidity = random.randint(40, 70)

    def GetData(self):
        with self.lock:
            # 딕셔너리 형태로 현재 센서 값 반환
            return {
                "name": self.name,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "temp": self.temperature,
                "light": self.illuminance,
                "humi": self.humidity
            }

# 센서 데이터 수집 쓰레드 함수
def sensor_data_collector(sensor_instance, interval_sec, data_queue):
    while True:
        sensor_instance.SetData()
        data = sensor_instance.GetData()
        
        # 1. 출력
        print(f"{data['timestamp']} {data['name']} - temp {data['temp']:02d}, light {data['light']:04d}, humi {data['humi']:02d}")
        
        # 3. 데이터 큐에 저장
        data_queue.put(data)
        
        time.sleep(interval_sec)

# 5개의 ParmSensor 인스턴스 생성
sensors = [ParmSensor(f"Parm-{i}") for i in range(1, 6)]
