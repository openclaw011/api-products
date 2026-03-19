"""
股票查询API - 可部署到RapidAPI
提供A股实时行情查询服务
"""

from flask import Flask, jsonify, request
import requests
from datetime import datetime
import json

app = Flask(__name__)

# 模拟股票数据（实际可对接真实数据源）
STOCK_DATA = {
    "000001": {"name": "平安银行", "price": 12.50, "change": 0.52, "change_pct": 4.33},
    "000002": {"name": "万科A", "price": 8.23, "change": -0.15, "change_pct": -1.79},
    "600000": {"name": "浦发银行", "price": 7.85, "change": 0.08, "change_pct": 1.03},
    "600036": {"name": "招商银行", "price": 35.60, "change": 0.45, "change_pct": 1.28},
    "000858": {"name": "五粮液", "price": 168.50, "change": 2.30, "change_pct": 1.38},
}

@app.route('/')
def index():
    """API首页"""
    return jsonify({
        "name": "A股查询API",
        "version": "1.0.0",
        "description": "提供A股实时行情查询服务",
        "endpoints": {
            "/stock/<code>": "查询单只股票",
            "/stocks": "查询所有股票列表",
            "/search/<keyword>": "按名称搜索股票",
            "/health": "健康检查"
        },
        "author": "AI助手",
        "pricing": "免费调用100次/月，超出后$0.01/次"
    })

@app.route('/stock/<code>')
def get_stock(code):
    """查询单只股票行情"""
    if code in STOCK_DATA:
        data = STOCK_DATA[code].copy()
        data['code'] = code
        data['timestamp'] = datetime.now().isoformat()
        return jsonify({
            "success": True,
            "data": data
        })
    return jsonify({
        "success": False,
        "error": f"股票代码 {code} 不存在"
    }), 404

@app.route('/stocks')
def get_all_stocks():
    """获取所有股票列表"""
    stocks = []
    for code, data in STOCK_DATA.items():
        stock = data.copy()
        stock['code'] = code
        stocks.append(stock)
    return jsonify({
        "success": True,
        "count": len(stocks),
        "data": stocks,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/search/<keyword>')
def search_stock(keyword):
    """按名称搜索股票"""
    results = []
    for code, data in STOCK_DATA.items():
        if keyword in data['name']:
            stock = data.copy()
            stock['code'] = code
            results.append(stock)
    return jsonify({
        "success": True,
        "keyword": keyword,
        "count": len(results),
        "data": results
    })

@app.route('/health')
def health():
    """健康检查"""
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
