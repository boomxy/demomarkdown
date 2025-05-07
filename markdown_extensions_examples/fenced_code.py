# 示例脚本: fenced_code
import markdown

# 初始化 Markdown 实例，启用 fenced_code 扩展
md = markdown.Markdown(extensions=["markdown.extensions.fenced_code"])

# 示例 Markdown 文本
sample_text = """# 示例标题

这是一个使用 fenced_code 扩展的示例。

下边是代码块

```
这是一行代码
```

上边是代码块

~~~
代码块的另外一种标识方式"~"，有可能和别的冲突
~~~

如果想显示三个反引号

````
```
````

直接跟列表项的代码块

* A list item.

```
not part of the list
```

为代码块增加属性

``` { attributes go here }
 带有属性的代码块
```

代码块属性 语言类型标记

``` { .html }
<p>HTML 文本</p>
```

或者，语言是指定的唯一选项，则可以排除花括号和/或圆点

``` { .html }
<p>HTML 文本</p>
```

除了语言之外，其他css 类 class 还可以通过在它们前面加点来定义，就像语言一样。

``` { .html .foo .bar }
<p>HTML Document</p>
```

css ID 的表示形式
``` { #example }
使用css 的 id 代码块
```

也可以混用css 的 ID 和  class
``` { #example .lang .foo .bar }
一个混用 css 的 id 和 class 的代码块
```

包括键值对，如果没有开启 [attr_list](/attr_list) 扩展, 键值对会被忽略
``` { .html #example style="color: #333; background: #f8f8f8;" }
一个带有样式的代码块， 如果没有开启 attr_list 扩展, 键值对会被忽略
```

同理，如果开启了 codehilight 插件，属性列表中定义的语言将传递给codehilite，以确保使用正确的语言，
``` { .python linenos=true linenostart=42 hl_lines="43-44 50" title="示例代码块" }
# 如果未指定语言并且未禁用codehilite扩展的语言猜测，则将猜测该语言。
```

[参考链接](https://python-markdown.github.io/extensions/fenced_code_blocks/)

"""

# 转换 Markdown 文本
html = md.convert(sample_text)

# 输出结果
print(html)
