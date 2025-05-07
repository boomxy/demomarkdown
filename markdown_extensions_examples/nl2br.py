# 示例脚本: nl2br
import markdown

# 初始化 Markdown 实例，启用 nl2br 扩展
md = markdown.Markdown(extensions=["markdown.extensions.nl2br"])

# 示例 Markdown 文本
sample_text = """# 强制换行扩展

这是一个使用 nl2br 强制换行扩展的示例。

以前，
这种紧挨着的两行会被渲染到一行上，忽略换行

现在，换行不
被忽略，会
根据文章内容加上换行标签

    会被转换成<br/>

空一行就新的 段落 p 

"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
