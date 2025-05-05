import markdown

md = markdown.Markdown(extensions=["meta"])

print(md.registeredExtensions)
res = md.convert("""\
---
title: h1
author: 1
---

# h1

p p""")
# print(md.Meta)
print(res)
