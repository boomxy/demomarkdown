# 示例脚本: wikilinks
import markdown

# 初始化 Markdown 实例，启用 wikilinks 扩展
md = markdown.Markdown(extensions=["markdown.extensions.wikilinks"])

# 示例 Markdown 文本
sample_text = """# 维基链接扩展

这是一个使用 wikilinks 维基链接扩展的示例。

    任何[[括号]]单词都会转换为链接

[[维基]]

一般情况下会和 [meta](/meta) 联合起来[使用](https://python-markdown.github.io/extensions/wikilinks/#using-with-meta-data-extension)
"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
