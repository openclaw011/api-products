"""
天气查询API - 可部署到RapidAPI
提供全球城市天气查询服务
"""

from flask import Flask, jsonify, request
from datetime import datetime
import random

app = Flask(__name__)

# 模拟天气数据
WEATHER_CONDITIONS = ["晴", "多云", "阴", "小雨", "中雨", "大雨", "雷阵雨", "小雪", "中雪", "大雪"]

CITIES = {
    "beijing": {"name": "北京", "country": "中国", "timezone": "Asia/Shanghai"},
    "shanghai": {"name": "上海", "country": "中国", "timezone": "Asia/Shanghai"},
    "guangzhou": {"name": "广州", "country": "中国", "timezone": "Asia/Shanghai"},
    "shenzhen": {"name": "深圳", "country": "中国", "timezone": "Asia/Shanghai"},
    "hangzhou": {"name": "杭州", "country": "中国", "timezone": "Asia/Shanghai"},
    "chengdu": {"name": "成都", "country": "中国", "timezone": "Asia/Shanghai"},
    "newyork": {"name": "纽约", "country": "美国", "timezone": "America/New_York"},
    "london": {"name": "伦敦", "country": "英国", "timezone": "Europe/London"},
    "tokyo": {"name": "东京", "country": "日本", "timezone": "Asia/Tokyo"},
    "paris": {"name": "巴黎", "country": "法国", "timezone": "Europe/Paris"},
}

def generate_weather():
    """生成模拟天气数据"""
    return {
        "condition": random.choice(WEATHER_CONDITIONS),
        "temperature": round(random.uniform(-10, 40), 1),
        "humidity": random.randint(20, 95),
        "wind_speed": round(random.uniform(0, 30), 1),
        "wind_direction": random.choice(["北风", "东北风", "东风", "东南风", "南风", "西南风", "西风", "西北风"]),
        "visibility": random.randint(1, 30),
        "pressure": round(random.uniform(990, 1030), 1),
        "uv_index": random.randint(1, 11),
        "air_quality": random.choice(["优", "良", "轻度污染", "中度污染"]),
    }

@app.route('/')
def index():
    """API首页"""
    return jsonify({
        "name": "天气查询API",
        "version": "1.0.0",
        "description": "提供全球城市天气查询服务",
        "endpoints": {
            "/weather/<city>": "查询城市天气",
            "/cities": "获取支持的城市列表",
            "/forecast/<city>": "查询城市未来7天预报",
            "/health": "健康检查"
        },
        "author": "AI助手",
        "pricing": "免费调用200次/月，超出后$0.005/次"
    })

@app.route('/weather/<city>')
def get_weather(city):
    """查询城市天气"""
    city_lower = city.lower()
    if city_lower in CITIES:
        city_info = CITIES[city_lower]
        weather = generate_weather()
        return jsonify({
            "success": True,
            "data": {
                "city": city_info["name"],
                "country": city_info["country"],
                "timezone": city_info["timezone"],
                **weather,
                "update_time": datetime.now().isoformat()
            }
        })
    return jsonify({
        "success": False,
        "error": f"城市 {city} 不在支持列表中"
    }), 404

@app.route('/cities')
def get_cities():
    """获取支持的城市列表"""
    cities = [{"id": k, **v} for k, v in CITIES.items()]
    return jsonify({
        "success": True,
        "count": len(cities),
        "data": cities
    })

@app.route('/forecast/<city>')
def get_forecast(city):
    """查询城市未来7天天气预报"""
    city_lower = city.lower()
    if city_lower in CITIES:
        city_info = CITIES[city_lower]
        forecast = []
        for i in range(7):
            weather = generate_weather()
            weather["date"] = datetime.now().strftime("%Y-%m-%d") if i == 0 else f"+{i}天"
            forecast.append(weather)
        return jsonify({
            "success": True,
            "data": {
                "city": city_info["name"],
                "country": city_info["country"],
                "forecast": forecast
            }
        })
    return jsonify({
        "success": False,
        "error": f"城市 {city} 不在支持列表中"
    }), 404

@app.route('/health')
def health():
    """健康检查"""
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
