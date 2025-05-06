# 示例脚本: abbr
import markdown

# 初始化 Markdown 实例，启用 abbr 扩展
md = markdown.Markdown(extensions=["markdown.extensions.abbr"])

# 示例 Markdown 文本
sample_text = """# 缩写扩展

这是一个使用 abbr 扩展(Abbreviations)的示例。

这句 HTML 被缩写，鼠标放上去会显示缩写的具体内容
这个 W3C 也是缩写的.

*[HTML]: 超文本标记语言 Hyper Text Markup Language
*[W3C]:  万维网联盟 World Wide Web Consortium
"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
