# 示例脚本: attr_list
import markdown

# 初始化 Markdown 实例，启用 attr_list 扩展
md = markdown.Markdown(extensions=["markdown.extensions.attr_list"])

# 示例 Markdown 文本
sample_text = """# 属性列表扩展

这是一个使用 attr_list 属性列表扩展的示例。

这是带有 id = "an_id" 的块
{: #an_id }

这是带有 class="a_class" 的块
{: .a_class }

要定义块级元素的属性，属性列表应在块的最后一行本身定义。
这是一个带有 id = "an_id" 和 class="a_class" 属性的块
{: #an_id .a_class }

这个新的块什么都没有，是默认的样式

## 标题是例外，允许写在一行上 {: .a_class } 

---

## 下边是内联元素，以超链接为例子

超链接也是可以写在一行上，要在内联元素上定义属性，应在内联元素之后立即定义属性列表，不得有空白。

[attr_list inline](https://python-markdown.github.io/extensions/attr_list/#inline){: class="a_class" title="这是标题!" }

这是有内联元素-> *内联元素*{: class="a_class" } <-且有样式的一行文字。

"""

# 转换 Markdown 文本
convert_html = md.convert(sample_text)

html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>属性列表扩展</title>
    <style>
        #an_id {{
            color: blue;
        }}
        
        .a_class {{
            background-color: lightgreen;
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
