# 示例脚本: sane_lists
import markdown

# 初始化 Markdown 实例，启用 sane_lists 扩展
md = markdown.Markdown(extensions=["markdown.extensions.sane_lists"])

# 示例 Markdown 文本
sample_text = """# 示例标题

这是一个使用 sane_lists 扩展的示例。
"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
