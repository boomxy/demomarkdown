# 示例脚本: tables
import markdown

# 初始化 Markdown 实例，启用 tables 扩展
md = markdown.Markdown(extensions=["markdown.extensions.tables"])

# 示例 Markdown 文本
sample_text = """# 表格扩展

这是一个使用 tables 表格扩展的示例。

这是一个表格

表头   |  表头2
----- | -----
 内容  | 内容
 内容  | 内容
"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
