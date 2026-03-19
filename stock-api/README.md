# A股查询API

> 部署到RapidAPI，提供A股实时行情查询服务

---

## 功能特性

- ✅ 查询单只股票行情
- ✅ 获取股票列表
- ✅ 按名称搜索股票
- ✅ 健康检查接口

---

## API端点

| 端点 | 方法 | 描述 |
|------|------|------|
| `/` | GET | API首页 |
| `/stock/<code>` | GET | 查询单只股票 |
| `/stocks` | GET | 获取所有股票列表 |
| `/search/<keyword>` | GET | 按名称搜索 |
| `/health` | GET | 健康检查 |

---

## 使用示例

### 查询单只股票
```bash
curl https://your-api.rapidapi.com/stock/000001
```

响应：
```json
{
  "success": true,
  "data": {
    "code": "000001",
    "name": "平安银行",
    "price": 12.50,
    "change": 0.52,
    "change_pct": 4.33,
    "timestamp": "2026-03-19T18:35:00"
  }
}
```

### 搜索股票
```bash
curl https://your-api.rapidapi.com/search/银行
```

---

## 定价

| 套餐 | 价格 | 调用次数 |
|------|------|---------|
| 免费版 | $0 | 100次/月 |
| 基础版 | $4.99 | 1000次/月 |
| 专业版 | $19.99 | 10000次/月 |
| 企业版 | $99.99 | 无限次 |

---

## 部署说明

1. 安装依赖：`pip install flask requests`
2. 运行：`python app.py`
3. 部署到Vercel/Railway/Render
4. 在RapidAPI上发布

---

## 作者

AI助手 🐂
