"""
提示词生成API - 可部署到RapidAPI
根据用户需求自动生成AI提示词
"""

from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)

# 提示词模板库
PROMPT_TEMPLATES = {
    "writing": {
        "name": "写作类",
        "templates": [
            "你是一位资深{style}作家。请写一篇关于{topic}的文章，风格要求{tone}，字数约{word_count}字。",
            "请根据以下主题创作一篇{type}：{topic}。要求：1. 结构清晰 2. 语言{style} 3. 有{element}元素",
            "你是一位专业的文案写手。请为{product}撰写一段{platform}文案，目标人群是{audience}，核心卖点是{selling_point}。",
        ]
    },
    "business": {
        "name": "商业类",
        "templates": [
            "你是一位商业顾问。请为{company_type}公司制定一份{plan_type}计划，包括：{elements}。",
            "请分析{industry}行业的市场机会，从以下维度展开：1. 市场规模 2. 竞争格局 3. 发展趋势 4. 机会点",
            "你是一位营销专家。请为{product}设计一套营销方案，目标市场是{market}，预算约{budget}。",
        ]
    },
    "learning": {
        "name": "学习类",
        "templates": [
            "你是一位{subject}老师。请用{level}学生能理解的语言，解释{concept}。",
            "请为{goal}设计一个{duration}天的学习计划，每天学习{hours}小时，重点包括：{topics}。",
            "你是一位记忆专家。请用记忆宫殿法，帮我记住{content}。要求：1. 形象化 2. 联想记忆 3. 便于回忆",
        ]
    },
    "coding": {
        "name": "编程类",
        "templates": [
            "你是一位{language}专家。请帮我实现一个{function}功能，要求：1. 代码简洁 2. 有注释 3. 有示例",
            "请review以下{language}代码，指出：1. 潜在bug 2. 性能问题 3. 优化建议 4. 最佳实践\n代码：{code}",
            "请为{project}项目设计架构，技术栈：{tech_stack}。要求：1. 模块化 2. 可扩展 3. 文档完善",
        ]
    },
    "creative": {
        "name": "创意类",
        "templates": [
            "你是一位创意总监。请为{brand}设计一个{type}创意方案，风格是{style}，受众是{audience}。",
            "请创作一个{genre}风格的故事，主角是{protagonist}，核心冲突是{conflict}，结局要{ending}。",
            "你是一位文案高手。请为{product}写{count}条slogan，要求：1. 简短有力 2. 突出卖点 3. 朗朗上口",
        ]
    },
}

@app.route('/')
def index():
    """API首页"""
    categories = {k: v["name"] for k, v in PROMPT_TEMPLATES.items()}
    return jsonify({
        "name": "提示词生成API",
        "version": "1.0.0",
        "description": "根据用户需求自动生成AI提示词",
        "categories": categories,
        "endpoints": {
            "/categories": "获取所有类别",
            "/generate": "生成提示词",
            "/templates/<category>": "获取某类别模板",
            "/health": "健康检查"
        },
        "author": "AI助手",
        "pricing": "免费调用500次/月，超出后$0.01/次"
    })

@app.route('/categories')
def get_categories():
    """获取所有类别"""
    categories = [{"id": k, "name": v["name"], "template_count": len(v["templates"])} 
                   for k, v in PROMPT_TEMPLATES.items()]
    return jsonify({
        "success": True,
        "count": len(categories),
        "data": categories
    })

@app.route('/templates/<category>')
def get_templates(category):
    """获取某类别模板"""
    if category in PROMPT_TEMPLATES:
        return jsonify({
            "success": True,
            "category": category,
            "name": PROMPT_TEMPLATES[category]["name"],
            "templates": PROMPT_TEMPLATES[category]["templates"]
        })
    return jsonify({
        "success": False,
        "error": f"类别 {category} 不存在"
    }), 404

@app.route('/generate', methods=['POST'])
def generate_prompt():
    """生成提示词"""
    data = request.json or {}
    category = data.get('category', 'writing')
    params = data.get('params', {})
    
    if category not in PROMPT_TEMPLATES:
        return jsonify({
            "success": False,
            "error": f"类别 {category} 不存在"
        }), 400
    
    templates = PROMPT_TEMPLATES[category]["templates"]
    
    # 根据模板生成提示词
    results = []
    for template in templates:
        try:
            prompt = template.format(**params)
            results.append(prompt)
        except KeyError as e:
            # 缺少参数时跳过
            continue
    
    return jsonify({
        "success": True,
        "category": category,
        "params": params,
        "count": len(results),
        "prompts": results,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/health')
def health():
    """健康检查"""
    return jsonify({
        "status": "ok",
        "timestamp": datetime.now().isoformat()
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002, debug=True)
