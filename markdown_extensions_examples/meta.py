# 示例脚本: meta
import markdown

# 初始化 Markdown 实例，启用 meta 扩展
md = markdown.Markdown(extensions=["markdown.extensions.meta"])

# 示例 Markdown 文本
sample_text = """---\
name: 元属性
type: 扩展
date: 2025-05-07
tags: 标签
      标
      签
---
# 元属性扩展

这是一个使用 meta 元属性扩展的示例。

meta 信息不会显示


元数据扩展添加了用于定义有关文档的元数据的语法。它的灵感来自MultiMarkdown的语法并遵循其语法。

目前，这个扩展不以任何方式使用元数据，只是将其作为Markdown实例的Meta属性提供给其他扩展或直接由您的python代码使用。[内容来源](https://python-markdown.github.io/extensions/meta_data/#summary)

[使用元数据的方式](https://python-markdown.github.io/extensions/meta_data/#accessing-the-meta-data)

"""

# 转换 Markdown 文本
convert_html = md.convert(sample_text)

html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>元属性</title>
</head>
<body>
{convert_html}
<hr />

<p>meta获取到的内容为: {md.Meta}</p>

<p>可以被 python 获取到: {md.Meta.keys()}</p>

遍历所有属性

<ul>
{''.join([f"<li>{key: <10} {': ' + ','.join(val)}</li>" for key, val in md.Meta.items()])}
</ul>

</body>
</body>
</html>"""



# 输出 meta 的值
print(md.Meta)
# 输出结果
print(html)
