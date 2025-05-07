# 示例脚本: legacy_attrs
import markdown

# 初始化 Markdown 实例，启用 legacy_attrs 扩展
md = markdown.Markdown(extensions=["markdown.extensions.legacy_attrs"])

# 示例 Markdown 文本
sample_text = """# 遗留/旧属性

这是一个使用 legacy_attrs 遗留/旧属性扩展的示例。

使用方式是

    {@key=value}

一句带有属性 {@class=foo} 定义在任意位置的，带有 class 属性, color: red;

一些 *增强{@id=bar}color: blue;* 带有 id 属性

![图片来源于 bing 壁纸（color: green）{@id=baz}](https://cn.bing.com/)
![图片来源于 bing 壁纸（color: green）{@id=baz}](https://cn.bing.com/th?id=OHR.DunluceIreland_ZH-CN2412229757_UHD.jpg&pid=hp&w=1920)

"""

# 转换 Markdown 文本
convert_html = md.convert(sample_text)

html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Markdown Extensions Example</title>
    <style>
     .foo {{
        color: red;
     }}
     
     #bar {{
         color: blue;
     }}
     
     #baz {{
        color: green; 
    }}
    </style>
</head>
<body>
    <div class="markdown-body">
       {convert_html}
    </div>
</body>
</html>
"""

# 输出结果
print(html)
