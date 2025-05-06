# 示例脚本: codehilite
import markdown

# 初始化 Markdown 实例，启用 codehilite 扩展
md = markdown.Markdown(extensions=["markdown.extensions.codehilite"])

# 示例 Markdown 文本
sample_text = """# 代码高亮

这是一个使用 codehilite 代码高亮扩展的示例。

CodeHilite 扩展使用 [Pygments](https://pygments.org/docs/quickstart/) 向标准 Python-Markdown 代码块添加代码/语法突出显示。
此扩展包含在标准Markdown库中。

## 步骤 1
安装 Pygments

## 步骤 2
使用 pygmentize -S default -f html -a .codehilite > styles.css 生成样式文件，供我们使用

## 步骤 3
编写内容， **注意使用缩进**


    :::python
    #!/usr/bin/python
    # 这里写代码 ...
    print('hello world')

另外的，指定第一行和第三行高亮

    :::python hl_lines="1 3"
    # 第 1 行是高亮
    # 第 2 行没有高亮
    # 第 3 行高亮
    hl_lines = [1, 3]

特殊情况，不指定语言，直接缩进

    # Code goes here ...

参考链接：[code_hilite](https://python-markdown.github.io/extensions/code_hilite/)
"""

# 转换 Markdown 文本
convert_html = md.convert(sample_text)

# 注意 style 部分是必须的，否则样式不生效。
html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>代码高亮</title>

    <style>
        /* 使用 pygmentize -S default -f html -a .codehilite > styles.css 命令生成的 css */
        pre {{ line-height: 125%; }}
td.linenos .normal {{ color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }}
span.linenos {{ color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }}
td.linenos .special {{ color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }}
span.linenos.special {{ color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }}
.codehilite .hll {{ background-color: #ffffcc }}
.codehilite {{ background: #f8f8f8; }}
.codehilite .c {{ color: #3D7B7B; font-style: italic }} /* Comment */
.codehilite .err {{ border: 1px solid #F00 }} /* Error */
.codehilite .k {{ color: #008000; font-weight: bold }} /* Keyword */
.codehilite .o {{ color: #666 }} /* Operator */
.codehilite .ch {{ color: #3D7B7B; font-style: italic }} /* Comment.Hashbang */
.codehilite .cm {{ color: #3D7B7B; font-style: italic }} /* Comment.Multiline */
.codehilite .cp {{ color: #9C6500 }} /* Comment.Preproc */
.codehilite .cpf {{ color: #3D7B7B; font-style: italic }} /* Comment.PreprocFile */
.codehilite .c1 {{ color: #3D7B7B; font-style: italic }} /* Comment.Single */
.codehilite .cs {{ color: #3D7B7B; font-style: italic }} /* Comment.Special */
.codehilite .gd {{ color: #A00000 }} /* Generic.Deleted */
.codehilite .ge {{ font-style: italic }} /* Generic.Emph */
.codehilite .ges {{ font-weight: bold; font-style: italic }} /* Generic.EmphStrong */
.codehilite .gr {{ color: #E40000 }} /* Generic.Error */
.codehilite .gh {{ color: #000080; font-weight: bold }} /* Generic.Heading */
.codehilite .gi {{ color: #008400 }} /* Generic.Inserted */
.codehilite .go {{ color: #717171 }} /* Generic.Output */
.codehilite .gp {{ color: #000080; font-weight: bold }} /* Generic.Prompt */
.codehilite .gs {{ font-weight: bold }} /* Generic.Strong */
.codehilite .gu {{ color: #800080; font-weight: bold }} /* Generic.Subheading */
.codehilite .gt {{ color: #04D }} /* Generic.Traceback */
.codehilite .kc {{ color: #008000; font-weight: bold }} /* Keyword.Constant */
.codehilite .kd {{ color: #008000; font-weight: bold }} /* Keyword.Declaration */
.codehilite .kn {{ color: #008000; font-weight: bold }} /* Keyword.Namespace */
.codehilite .kp {{ color: #008000 }} /* Keyword.Pseudo */
.codehilite .kr {{ color: #008000; font-weight: bold }} /* Keyword.Reserved */
.codehilite .kt {{ color: #B00040 }} /* Keyword.Type */
.codehilite .m {{ color: #666 }} /* Literal.Number */
.codehilite .s {{ color: #BA2121 }} /* Literal.String */
.codehilite .na {{ color: #687822 }} /* Name.Attribute */
.codehilite .nb {{ color: #008000 }} /* Name.Builtin */
.codehilite .nc {{ color: #00F; font-weight: bold }} /* Name.Class */
.codehilite .no {{ color: #800 }} /* Name.Constant */
.codehilite .nd {{ color: #A2F }} /* Name.Decorator */
.codehilite .ni {{ color: #717171; font-weight: bold }} /* Name.Entity */
.codehilite .ne {{ color: #CB3F38; font-weight: bold }} /* Name.Exception */
.codehilite .nf {{ color: #00F }} /* Name.Function */
.codehilite .nl {{ color: #767600 }} /* Name.Label */
.codehilite .nn {{ color: #00F; font-weight: bold }} /* Name.Namespace */
.codehilite .nt {{ color: #008000; font-weight: bold }} /* Name.Tag */
.codehilite .nv {{ color: #19177C }} /* Name.Variable */
.codehilite .ow {{ color: #A2F; font-weight: bold }} /* Operator.Word */
.codehilite .w {{ color: #BBB }} /* Text.Whitespace */
.codehilite .mb {{ color: #666 }} /* Literal.Number.Bin */
.codehilite .mf {{ color: #666 }} /* Literal.Number.Float */
.codehilite .mh {{ color: #666 }} /* Literal.Number.Hex */
.codehilite .mi {{ color: #666 }} /* Literal.Number.Integer */
.codehilite .mo {{ color: #666 }} /* Literal.Number.Oct */
.codehilite .sa {{ color: #BA2121 }} /* Literal.String.Affix */
.codehilite .sb {{ color: #BA2121 }} /* Literal.String.Backtick */
.codehilite .sc {{ color: #BA2121 }} /* Literal.String.Char */
.codehilite .dl {{ color: #BA2121 }} /* Literal.String.Delimiter */
.codehilite .sd {{ color: #BA2121; font-style: italic }} /* Literal.String.Doc */
.codehilite .s2 {{ color: #BA2121 }} /* Literal.String.Double */
.codehilite .se {{ color: #AA5D1F; font-weight: bold }} /* Literal.String.Escape */
.codehilite .sh {{ color: #BA2121 }} /* Literal.String.Heredoc */
.codehilite .si {{ color: #A45A77; font-weight: bold }} /* Literal.String.Interpol */
.codehilite .sx {{ color: #008000 }} /* Literal.String.Other */
.codehilite .sr {{ color: #A45A77 }} /* Literal.String.Regex */
.codehilite .s1 {{ color: #BA2121 }} /* Literal.String.Single */
.codehilite .ss {{ color: #19177C }} /* Literal.String.Symbol */
.codehilite .bp {{ color: #008000 }} /* Name.Builtin.Pseudo */
.codehilite .fm {{ color: #00F }} /* Name.Function.Magic */
.codehilite .vc {{ color: #19177C }} /* Name.Variable.Class */
.codehilite .vg {{ color: #19177C }} /* Name.Variable.Global */
.codehilite .vi {{ color: #19177C }} /* Name.Variable.Instance */
.codehilite .vm {{ color: #19177C }} /* Name.Variable.Magic */
.codehilite .il {{ color: #666 }} /* Literal.Number.Integer.Long */

    </style>
</head>
<body>
    {convert_html}
</body>
</html>
"""

# 输出结果
print(html)
