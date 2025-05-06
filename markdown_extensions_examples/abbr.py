# 示例脚本: abbr
import markdown

# 初始化 Markdown 实例，启用 abbr 扩展
md = markdown.Markdown(extensions=["markdown.extensions.abbr"])

# 示例 Markdown 文本
sample_text = """# 示例标题

这是一个使用 abbr 扩展的示例。

The HTML specification
is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]:  World Wide Web Consortium
"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
