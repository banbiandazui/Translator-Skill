"""
Translator Skill

功能：
简单文本翻译助手
"""

def translate(text, target_language="English"):

    result = f"""
翻译目标语言：{target_language}

原文：
{text}

翻译结果：
（此处由AI模型完成实际翻译）

同时请注意：
- 保持原文含义
- 保留专业术语
- 根据语境调整表达
"""

    return result


if __name__ == "__main__":

    text = input("请输入需要翻译的内容：")

    language = input("请输入目标语言：")

    print(translate(text, language))
