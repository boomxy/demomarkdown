# 示例脚本: footnotes
import markdown

# 初始化 Markdown 实例，启用 footnotes 扩展
md = markdown.Markdown(extensions=["markdown.extensions.footnotes"])

# 示例 Markdown 文本
sample_text = """# 脚注扩展

这是一个使用 footnotes 脚注扩展的示例。

脚注[^1] 有一个标签[^@#$%] 还有脚注内容组成。

脚注[^2] 的内容可以是多行的。

将

内

容

和

脚

注

分

开

。

。

。

。

。

。

。

。

可

以

点

*↩*

来

回

跳

转


[^1]: 这是脚注的内容
[^@#$%]: 脚注的标签: "@#$%"
[^2]:
    第一句定义。

    第二句定义。

    > 一个多行的
    > 块。

        一个代码块

    最后一句。
"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
