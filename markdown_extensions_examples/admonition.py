# 示例脚本: admonition
import markdown

# 初始化 Markdown 实例，启用 admonition 扩展
md = markdown.Markdown(extensions=["markdown.extensions.admonition"])

# 示例 Markdown 文本
sample_text = """# 警告框扩展 admonition 

这是一个使用 admonition 扩展的示例。

!!! note "双引号中的可选显式标题"
    任何数量的其他缩入markdown元素。
    这是第二段。

新的一段

!!! danger "这个标题是可省略的"
    您应该注意，标题将自动大写。

!!! important ""
    这是一个没有标题的警告框

!!! danger highlight blink "highlight和blink 都是 css 样式"
    highlight和blink 都是 css class 样式，有更多的可以继续往后写
"""

# 转换 Markdown 文本
convert_html = md.convert(sample_text)
# 完整的 HTML 页面模板
html = f"""
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>Admonition 示例</title>
    <style>
        .admonition {{
            padding: 1em;
            margin: 1em 0;
            border-radius: 5px;
        }}

        .admonition.note {{
            background-color: #e6f7ff;
            border-left: 6px solid #409EFF;
        }}

        .admonition.danger {{
            background-color: #fff0f0;
            border-left: 6px solid #ff4d4f;
        }}

        .admonition.important {{
            background-color: #fffbe6;
            border-left: 6px solid #faad14;
        }}
    </style>
</head>
<body>
    {convert_html}
</body>
</html>
"""
# 输出结果
print(html)
