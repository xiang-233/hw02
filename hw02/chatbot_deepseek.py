# -*- coding: utf-8 -*-
from openai import OpenAI
import os

def doubao_chatbot(api_key: str, user_query: str, model: str = "Doubao-Seed-2.0-pro") -> str:
    """
    调用 豆包（火山方舟）API 实现简单 Chatbot
    :param api_key: 火山方舟 API Key
    :param user_query: 用户输入问题
    :param model: 模型名称（需与火山方舟后台一致）
    :return: 模型回复
    """
    try:
        # 初始化客户端（兼容 OpenAI SDK）
        client = OpenAI(
            api_key=api_key,
            base_url="https://ark.cn-beijing.volces.com/api/v3"  # 火山方舟接口地址
        )
        # 构建对话参数
        messages = [
            {"role": "system", "content": "你是一个专业的航空工程AI助手,回答准确\简洁,提供具体数值与单位"},
            {"role": "user", "content": user_query}
        ]
        # 调用模型
        response = client.chat.completions.create(
            model="doubao-seed-2-0-pro-260215",
            messages=messages,
            temperature=0.3,  # 降低创意度，保证数据准确
            max_tokens=1024,
            stream=False
        )
        # 解析回复
        reply = response.choices[0].message.content
        return reply
    except Exception as e:
        return f"调用失败：{str(e)}"

# 主函数（可直接运行）
if __name__ == "__main__":
    # 配置 API Key（建议通过环境变量获取,避免硬编码）
    ARK_API_KEY = "9c2f68e6-ed1c-46f9-93fe-ade7c6820244"
    
    # 用户输入问题：波音737的起飞临界速度是多少
    user_input = "波音737的起飞临界速度是多少"
    
    # 调用机器人
    result = doubao_chatbot(ARK_API_KEY, user_input)
    
    # 输出结果
    print("\n豆包 关于波音737起飞临界速度的回复：")
    print(result)