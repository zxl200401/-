from flask import Flask, jsonify, request
from models import ContentGenerator, CampaignManager, PerformanceAnalyzer

app = Flask(__name__)

# 创建一个广告内容生成器
content_generator = ContentGenerator()

# 创建广告投放策略管理器
campaign_manager = CampaignManager()

# 创建广告效果分析器
performance_analyzer = PerformanceAnalyzer()

@app.route('/generate_ad', methods=['POST'])
def generate_ad():
    ad_data = content_generator.generate_ad()
    return jsonify(ad_data)

@app.route('/optimize_campaign', methods=['POST'])
def optimize_campaign():
    campaign_data = request.json
    optimized_campaign = campaign_manager.optimize_campaign(campaign_data)
    return jsonify(optimized_campaign)

@app.route('/analyze_performance', methods=['POST'])
def analyze_performance():
    ad_data = request.json
    performance_report = performance_analyzer.analyze_performance(ad_data)
    return jsonify(performance_report)

if __name__ == "__main__":
    app.run(debug=True)
