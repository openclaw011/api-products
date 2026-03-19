# 部署到 Railway 指南

> 使用邮箱：775899lixiao@gmail.com

---

## 步骤 1：注册 Railway

1. 访问 https://railway.app
2. 点击 "Start for Free"
3. 选择 "Continue with GitHub"
4. 授权 Railway 访问你的 GitHub

---

## 步骤 2：部署股票API

1. 在 Railway 仪表板点击 "New Project"
2. 选择 "Deploy from GitHub repo"
3. 选择 `api-products` 仓库
4. 点击 "Add Variables" 添加环境变量（可选）
5. 点击 "Deploy"

**注意**：需要在根目录创建 `railway.json` 指定启动命令

---

## 步骤 3：获取API地址

部署成功后：
1. 点击项目进入详情
2. 在 "Deployments" 找到域名
3. 例如：`https://stock-api-production.up.railway.app`

---

## 步骤 4：测试API

```bash
curl https://your-domain/stock/000001
```

---

## 步骤 5：发布到 RapidAPI

1. 访问 https://rapidapi.com
2. 用 Gmail 登录
3. 点击 "Add API"
4. 填写信息：
   - Name: A股查询API
   - Description: 提供A股实时行情查询
   - Base URL: Railway部署的地址
5. 添加端点：
   - GET /stock/{code}
   - GET /stocks
   - GET /search/{keyword}
6. 设置定价：
   - Free: 100次/月
   - Basic: $4.99/1000次
   - Pro: $19.99/10000次
7. 发布！

---

## 定价建议

| 套餐 | 价格 | 调用次数 | 说明 |
|------|------|---------|------|
| Free | $0 | 100次/月 | 引流用 |
| Basic | $4.99 | 1000次 | 个人开发者 |
| Pro | $19.99 | 10000次 | 小型企业 |
| Enterprise | $99.99 | 无限 | 企业客户 |

---

## 预期收入

假设每个API每天100次付费调用：
- 3个API × 100次 × $0.01 = $3/天
- 月收入：约 $90
- 扩展到10个API：约 $300/月

---

## 后续优化

1. 对接真实股票数据源（TuShare/东方财富）
2. 增加更多API（翻译/OCR/二维码等）
3. 优化性能和稳定性

---

**作者：AI助手 🐂**
