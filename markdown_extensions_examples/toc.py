# 示例脚本: toc
import markdown

# 初始化 Markdown 实例，启用 toc 扩展
md = markdown.Markdown(extensions=["markdown.extensions.toc"])

# 示例 Markdown 文本
sample_text = """# 目录扩展

这是一个使用 toc 目录扩展的示例。

[使用参考](https://python-markdown.github.io/extensions/toc/#usage)

下边是内容，目录扩展生效位置在下边

内容。。。
内容。。。。

内容。
内容。。。

# 一级目录 1
内容。。。
内容。。。。

## 二级目录 1.1
内容。。。


## 二级目录 1.2

内容。。。

## 二级目录 1.3

内容。。。

# 一级目录 2

内容。。。

## 二级目录 2.1

内容。。。

## 二级目录 2.2

内容。。。


---

这里放目录：

[TOC]

"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
