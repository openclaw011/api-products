# 提示词生成API

> 部署到RapidAPI，自动生成AI提示词

---

## 功能特性

- ✅ 5大类别模板
- ✅ 动态参数填充
- ✅ 批量生成提示词
- ✅ 支持自定义需求

---

## 支持类别

| 类别 | 描述 |
|------|------|
| writing | 写作类提示词 |
| business | 商业类提示词 |
| learning | 学习类提示词 |
| coding | 编程类提示词 |
| creative | 创意类提示词 |

---

## API端点

| 端点 | 方法 | 描述 |
|------|------|------|
| `/` | GET | API首页 |
| `/categories` | GET | 获取所有类别 |
| `/templates/<category>` | GET | 获取模板 |
| `/generate` | POST | 生成提示词 |
| `/health` | GET | 健康检查 |

---

## 使用示例

### 生成提示词
```bash
curl -X POST https://your-api.rapidapi.com/generate \
  -H "Content-Type: application/json" \
  -d '{
    "category": "writing",
    "params": {
      "style": "幽默",
      "topic": "程序员的生活",
      "tone": "轻松",
      "word_count": 800
    }
  }'
```

响应：
```json
{
  "success": true,
  "count": 1,
  "prompts": [
    "你是一位资深幽默作家。请写一篇关于程序员的生活的文章，风格要求轻松，字数约800字。"
  ]
}
```

---

## 定价

| 套餐 | 价格 | 调用次数 |
|------|------|---------|
| 免费版 | $0 | 500次/月 |
| 基础版 | $4.99 | 5000次/月 |
| 专业版 | $19.99 | 50000次/月 |

---

## 作者

AI助手 🐂
