# 天气查询API

> 部署到RapidAPI，提供全球城市天气查询服务

---

## 功能特性

- ✅ 查询实时天气
- ✅ 支持10+主要城市
- ✅ 7天天气预报
- ✅ 空气质量指数

---

## API端点

| 端点 | 方法 | 描述 |
|------|------|------|
| `/` | GET | API首页 |
| `/weather/<city>` | GET | 查询城市天气 |
| `/cities` | GET | 获取支持的城市 |
| `/forecast/<city>` | GET | 7天预报 |
| `/health` | GET | 健康检查 |

---

## 使用示例

### 查询天气
```bash
curl https://your-api.rapidapi.com/weather/beijing
```

响应：
```json
{
  "success": true,
  "data": {
    "city": "北京",
    "country": "中国",
    "condition": "晴",
    "temperature": 25.3,
    "humidity": 45,
    "wind_speed": 3.2,
    "wind_direction": "北风",
    "visibility": 15,
    "uv_index": 6,
    "air_quality": "良",
    "update_time": "2026-03-19T18:35:00"
  }
}
```

---

## 定价

| 套餐 | 价格 | 调用次数 |
|------|------|---------|
| 免费版 | $0 | 200次/月 |
| 基础版 | $2.99 | 2000次/月 |
| 专业版 | $9.99 | 20000次/月 |

---

## 作者

AI助手 🐂
