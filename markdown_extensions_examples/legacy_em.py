# 示例脚本: legacy_em
import markdown

# 初始化 Markdown 实例，启用 legacy_em 扩展
md = markdown.Markdown(extensions=["markdown.extensions.legacy_em"])

# 示例 Markdown 文本
sample_text = """# 旧的倾斜扩展

这是一个使用 legacy_em 传统/旧倾斜扩展的示例。

    原本的样子是 _连_接_

当使用下划线的时候 _连_接_ 这样的文字 会被替换



或者期望的效果 *连_接* 这样
"""

# 转换 Markdown 文本
convert_html = md.convert(sample_text)

html = f"""<html>
<head>
<style>
em {{
   color: red;
   font-size:2em;
}}
</style>
</head>
<body>
{convert_html}
</body>
</html>"""

# 输出结果
print(html)
