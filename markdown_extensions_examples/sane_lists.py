# 示例脚本: sane_lists
import markdown

# 初始化 Markdown 实例，启用 sane_lists 扩展
md = markdown.Markdown(extensions=["markdown.extensions.sane_lists"])

# 示例 Markdown 文本
sample_text = """# Sane 列表扩展

这是一个使用 sane_lists Sane 列表扩展的示例。

下边是两种定义列表的方式

1. 有序列表项 1
2. 有序列表项 2

* 无序列表项 1
* 无序列表项 2

默认的Markdown行为是生成无序列表。

请注意，与默认的Markdown行为不同，如果列表项之间不包括白线，则会完全忽略不同的列表类型。这与段落的行为相对应。例如：

A Paragraph.
* Not a list item.

1. Ordered list item.
* Not a separate list item.

理智的列表还识别有序列表中使用的数字。给出以下列表：

4. Apples
5. Oranges
6. Pears

默认情况下，markdown将忽略第一行以项目号“4”开始而HTML列表将以数字“1”开始

"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
