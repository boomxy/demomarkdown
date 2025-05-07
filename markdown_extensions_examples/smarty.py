# 示例脚本: smarty
import markdown

# 初始化 Markdown 实例，启用 smarty 扩展
md = markdown.Markdown(extensions=["markdown.extensions.smarty"])

# 示例 Markdown 文本
sample_text = """# 智能类型扩展

这是一个使用 smarty 智能类型扩展的示例。

智能类型扩展会转换 ASCII 码中的

    '  "  << >>  ...  --  ---

这些类型 转换为 html 对应的等效 HTML 实体:
 
 &lsquo;&rsquo; &nbsp;&nbsp; &ldquo; &rdquo;  &nbsp;&nbsp; &laquo; &raquo;  &nbsp;&nbsp; &hellip;  &nbsp;&nbsp; &ndash;  &nbsp;&nbsp; &mdash;

[使用参考](https://python-markdown.github.io/extensions/smarty/#usage)
"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
