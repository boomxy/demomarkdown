# 示例脚本: def_list
import markdown

# 初始化 Markdown 实例，启用 def_list 扩展
md = markdown.Markdown(extensions=["markdown.extensions.def_list"])

# 示例 Markdown 文本
sample_text = """# 定义列表扩展

这是一个使用 def_list 定义列表扩展的示例。

注意：折叠功能是我们自己实现的，不是自动生成的

苹果🍎
:   苹果属植物的果类果实
    迷迭香科。
:   新的苹果品种

橘子🍊
:   柑橘属常绿树的果实。
:   大橙子
:   大柚子
"""

# 转换 Markdown 文本
convert_html = md.convert(sample_text)

html = f"""
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="UTF-8">
    <title>Admonition 示例</title>
    <style>
        dl dt {{
            cursor: pointer;
            background-color: #f0f0f0;
            padding: 10px;
        }}
        dl dd {{
            display: none;
            padding: 10px;
        }}
        dl dd.open {{
            display: block;
        }}
        
        /* 使用伪元素添加展开/折叠图标 */
        dl dt::before {{
          content: "▶"; /* 默认展开图标 */
          position: absolute;
          left: 5px;
          transition: transform 0.2s ease;
        }}
        
        /* 展开状态时的图标 */
        dl dt.open::before {{
          content: "▼"; /* 折叠图标 */
        }}
    </style>
</head>
<body>
    {convert_html}
   <script>
        document.addEventListener("DOMContentLoaded", function() {{
            const terms = document.querySelectorAll("dl dt");
            terms.forEach(term => {{
                term.addEventListener("click", () => {{
                    let next = term.nextElementSibling; 
                     const isOpen = term.classList.contains("open");

                    // 切换当前 dt 的 open 类
                     term.classList.toggle("open", !isOpen);
                     while (next && next.tagName.toLowerCase() !== 'dt') {{
                        if (next.tagName.toLowerCase() === 'dd') {{
                            next.classList.toggle("open");
                        }}
                        next = next.nextElementSibling;
                     }}
                }});
            }});
        }});
    </script>
</body>

"""

# 输出结果
print(html)
