import markdown

from markdown.extensions import extra
# 示例脚本: extra

# 初始化 Markdown 实例，启用 abbr 扩展
md = markdown.Markdown(extensions=["markdown.extensions.extra"])

# 示例 Markdown 文本
sample_text = """# 标准扩展

这是一个使用 extra 标准扩展的示例。

如果开启了使用了这个 extra 标准扩展，相当于一次性启用了如下扩展:

- [fenced_code](/fenced_code)
- [footnotes](/footnotes)
- [attr_list](/attr_list)
- [def_list](/def_list)
- [tables](/tables)
- [abbr](/abbr)
- [md_in_html](/abbr)

这是 footnotes[^1] 示例:

这是 fenced_code 示例:

```
这是一行fenced_code代码
```

这是一个 attr_list 示例{class="a_class"}, 在生成的元素里会有出现

这是 def_list 示例：

苹果🍎
:   苹果属植物的果类果实
    迷迭香科。
:   新的苹果品种

这是 tables 示例：

表头   |  表头2
----- | -----
 内容  | 内容
 内容  | 内容

这是 abbr 示例

这个 ABBR 是缩写的。
*[ABBR]:  缩写的意思

这是 md_in_html 示例:

<div markdown="1" style="color:red">*倾斜字体* markdown 写法</div>


[^1]: 开启了此扩展

"""

# 转换 Markdown 文本
html = md.convert(sample_text)

print("开启了这些扩展", extra.extensions)
# 输出结果
print(html)
