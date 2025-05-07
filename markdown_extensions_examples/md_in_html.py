# 示例脚本: md_in_html
import markdown

# 初始化 Markdown 实例，启用 md_in_html 扩展
md = markdown.Markdown(extensions=["markdown.extensions.md_in_html"])

# 示例 Markdown 文本
sample_text = """# 在 html 标签里的 markdown 扩展

这是一个使用 md_in_html 在 html 标签里的 markdown 扩展的示例。

使用方式是在 html 标签上增加 markdown = "1" 或者 "block"或者 "span"。

这是一个 markdown="1" 的示例:

<div markdown="1">
这里的倾斜 *Markdown* 就是被渲染的.
</div>

这是一个 markdown="block" 的示例:

<section markdown="block">
# 标题

一个 *Markdown* 被倾斜的句子

* 列表项
* 另外一个列表项

</section>

这是一个 markdown="span" 的示例:

<div markdown="span">
# *不是* 一个标题， 只渲染了 em
</div>

当 markdown 的属性为 canvas、math、select、pro、title和textarea 的时候会被忽略，[参见](https://python-markdown.github.io/extensions/md_in_html/#ignored-elements)

当嵌套多层原始HTML元素时，必须为每个块级元素定义markdown属性。对于任何没有markdown属性的块级元素，该元素内部的所有内容都会被忽略，包括具有markdown属性的子元素。[参见](https://python-markdown.github.io/extensions/md_in_html/#nesting)

一个嵌套多层的例子:

<article id="my-article" markdown="1">
# 最外层文章的标题

 markdown的属性为 1，下边有嵌套的子元素也必须重新增加 markdown 属性.

<section id="section-1" markdown="1">
## 第 1 个章节的标题

<p>原始的 markdown 内容 **HTML** 会被忽略，因为没有指定 markdown 属性</p>

</section>

<section id="section-2" markdown="1">
## 第 2 个章节的标题

<p markdown="1">**Markdown** 内容会被渲染，因为指定了markdown="1"</p>

</section>

</article>

---

标签级别的规范：
<div markdown="1">
<p markdown="1">一个 包含 markdown *没有* 闭合标签但是指定了markdown="1"的例子
<p>这里也 *没有* 闭合标签，并且 *没有* 指定markdown="1"
</div>

"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
