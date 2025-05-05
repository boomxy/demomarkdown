# 示例脚本: fenced_code
import markdown

# 初始化 Markdown 实例，启用 fenced_code 扩展
md = markdown.Markdown(extensions=["markdown.extensions.fenced_code"])

# 示例 Markdown 文本
sample_text = """# 示例标题

这是一个使用 fenced_code 扩展的示例。
"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
