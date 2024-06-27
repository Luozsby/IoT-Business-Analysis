from django.shortcuts import render,HttpResponse,redirect

from mqttapp.models import UserInfo
from .models import SensorData

# Create your views here.
def index(request):
    return HttpResponse('欢迎使用')

def login(request):
    if request.method=="GET":
        return render(request,"login.html")
    username = request.POST.get('username')
    password = request.POST.get('password')
    if (username=='iot' and password=='123') :
    # 在这里可以对用户名和密码进行进一步的验证或处理
        return redirect('http://127.0.0.1:8000/info/list')
    elif UserInfo.objects.filter(name=username, password=password).exists():
        return redirect('http://127.0.0.1:8000/sensor_data')
        
    return render(request,'login.html',{'error_msg':'用户名或密码错误'}) 


def info_list(request):
    #获取数据库中所有用户信息
    data_list=UserInfo.objects.all()
    return render(request,'info_list.html',{'data_list': data_list})


def info_add(request):
    if request.method == "GET":
        return render(request,'info_add.html')
    name = request.POST.get('name')
    password = request.POST.get('password')
    age = request.POST.get('age')
    if not name or not password or not age:
        return HttpResponse('请你填完整')
    try:
        age = int(age)
    except ValueError:
        return HttpResponse("年龄必须是一个整数", status=400)
    # 保存到数据库
    UserInfo.objects.create(name=name, password=password, age=age)
    return redirect('http://127.0.0.1:8000/info/list')
  

def info_delete(request):
    nid=request.GET.get('nid')
    UserInfo.objects.filter(id=nid).delete()
    return redirect('http://127.0.0.1:8000/info/list')


def sensor_data(request):
    data = SensorData.objects.all().order_by('-timestamp')[:2]
    return render(request, 'sensor_data.html', {'data': data})



import json
import paho.mqtt.publish as publish
from django.http import JsonResponse
def mqtt_publish(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            topic = data.get('topic')
            message = data.get('message')
            # 发布消息到 MQTT 主题
            publish.single(topic, message, hostname="111.230.201.180",
                           auth={'username': "iot", 'password': "iot123456"})
            return JsonResponse({'message': '消息发布成功'})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': '仅支持 POST 请求'}, status=405)
    


from django.http import JsonResponse
from mqttapp.models import SensorData

def get_sensor_data(request):
    data = SensorData.objects.order_by('-timestamp')[:1]
    response_data = [
        {
            'timestamp': entry.timestamp,
            'temperature': entry.temperature,
            'humidity': entry.humidity
        }
        for entry in data
    ]
    return JsonResponse(response_data, safe=False)


from django.shortcuts import render
from django.http import JsonResponse
from .models import SensorData

def get_all_sensor_data(request):
    sensor_data = SensorData.objects.all().order_by('timestamp')  # 获取所有传感器数据，按时间戳排序
    data = list(sensor_data.values())  # 将查询集转换为字典列表
    return JsonResponse(data, safe=False)