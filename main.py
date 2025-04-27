from markdown import Markdown


def main():
    md = Markdown()

    #  h1-h6
    for i in (1, 2, 3, 4, 5, 6):
        res = md.convert(f"{'#' * i} h{i}")
        print(res)

    # p
    res = md.convert("p p")
    print(res)

    # ul *
    res = md.convert("* a\n* b\n* c")
    print(res)

    # ul -
    res = md.convert("- a\n- b\n- c")
    print(res)

    # ul +
    res = md.convert("- a\n- b\n- c")
    print(res)

    # ol
    res = md.convert("1. a\n2. b\n3. c")
    print(res)

    # strong
    res = md.convert("**strong**")
    print(res)

    # em
    res = md.convert("*em*")
    print(res)

    # code
    res = md.convert("`print('code')`")
    print(res)

    # hr ---
    res = md.convert("---")
    print(res)

    # hr ***
    res = md.convert("***")
    print(res)



if __name__ == '__main__':
    main()
