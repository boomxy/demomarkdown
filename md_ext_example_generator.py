import os
import markdown
from markdown.extensions import Extension

class MyExtension(Extension):
    def extendMarkdown(self, md):
        # 在这里添加你的扩展逻辑
        pass

'''
这个脚本是创建一个目录，并在该目录下为每个 Markdown 扩展生成一个示例脚本。
'''

# 获取所有自带的扩展
extensions = [
    "markdown.extensions.abbr",
    "markdown.extensions.attr_list",
    "markdown.extensions.def_list",
    "markdown.extensions.fenced_code",
    "markdown.extensions.footnotes",
    "markdown.extensions.md_in_html",
    "markdown.extensions.tables",
    "markdown.extensions.admonition",
    "markdown.extensions.codehilite",
    "markdown.extensions.legacy_attrs",
    "markdown.extensions.legacy_em",
    "markdown.extensions.meta",
    "markdown.extensions.nl2br",
    "markdown.extensions.sane_lists",
    "markdown.extensions.smarty",
    "markdown.extensions.toc",
    "markdown.extensions.wikilinks",
]

# 创建一个目录存放示例脚本
output_dir = "markdown_extensions_examples"
os.makedirs(output_dir, exist_ok=True)

# 为每个扩展创建一个示例脚本
for ext in extensions:
    ext_name = ext.split(".")[-1]
    file_path = os.path.join(output_dir, f"{ext_name}.py")
    with open(file_path, "w") as f:
        f.write(f"""\
# 示例脚本: {ext_name}
import markdown

# 初始化 Markdown 实例，启用 {ext_name} 扩展
md = markdown.Markdown(extensions=["{ext}"])

# 示例 Markdown 文本
sample_text = \"\"\"\
# 示例标题

这是一个使用 {ext_name} 扩展的示例。
\"\"\"

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
""")
    print(f"已生成示例脚本: {file_path}")

# 添加 pymdown-extensions 扩展
pymdown_extensions = [
    "pymdownx.arithmatex",
    "pymdownx.betterem",
    "pymdownx.caret",
    "pymdownx.critic",
    "pymdownx.details",
    "pymdownx.emoji",
    "pymdownx.highlight",
    "pymdownx.inlinehilite",
    "pymdownx.keys",
    "pymdownx.magiclink",
    "pymdownx.mark",
    "pymdownx.smartsymbols",
    "pymdownx.superfences",
    "pymdownx.tasklist",
    "pymdownx.tilde",
]

# 更新输出目录
output_dir = "pymdown_extensions_examples"
os.makedirs(output_dir, exist_ok=True)

# 为每个 pymdown-extensions 扩展创建一个示例脚本
for ext in pymdown_extensions:
    ext_name = ext.split(".")[-1]
    file_path = os.path.join(output_dir, f"{ext_name}.py")
    with open(file_path, "w") as f:
        f.write(f"""\
# 示例脚本: {ext_name}
import markdown

# 初始化 Markdown 实例，启用 {ext_name} 扩展
md = markdown.Markdown(extensions=["{ext}"])

# 示例 Markdown 文本
sample_text = \"\"\"\
# 示例标题

这是一个使用 {ext_name} 扩展的示例。
\"\"\"

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
""")
    print(f"已生成示例脚本: {file_path}")

