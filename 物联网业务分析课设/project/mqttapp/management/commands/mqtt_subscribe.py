import paho.mqtt.client as mqtt
from django.core.management.base import BaseCommand
from mqttapp.models import SensorData

# MQTT回调函数，当客户端连接时调用
def on_connect(client, userdata, flags, rc):
    print("连接结果代码: " + str(rc))
    client.subscribe("2140707159")  # 订阅主题

# MQTT回调函数，当接收到消息时调用
def on_message(client, userdata, msg):
    payload = msg.payload.decode()  # 解码消息
    temperature, humidity = map(float, payload.split(' '))  # 解析温度和湿度
    SensorData.objects.create(temperature=temperature, humidity=humidity)  # 存储到数据库
    print(f"温度: {temperature}, 湿度: {humidity}")

# 自定义管理命令
class Command(BaseCommand):
    help = '启动MQTT订阅器以接收传感器数据'

    def handle(self, *args, **kwargs):
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message

        # 连接到MQTT代理
        mqtt_broker_address = "111.230.201.180"
        client.username_pw_set("iot", "iot123456")  # 设置用户名和密2140707159
        client.connect(mqtt_broker_address, 1883, 60)  # 连接到MQTT代理
        client.loop_forever()  # 保持订阅连接