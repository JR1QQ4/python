#! python3
# 利用一个关键字保存每段剪贴板文本
# 当运行 py mcb.pyw save spam， 剪贴板中当前的内容就用关键字 spam 保存
# 运行 py mcb.pyw spam， 这段文本稍后将重新加载到剪贴板中
# 如果用户忘记了都有哪些关键字， 他们可以运行 py mcb.pyw list，将所有关键字的列表复制到剪贴板中
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        if sys.argv[2] in mcbShelf:
            del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    if sys.argv[1].lower() == 'delete':
        for item in mcbShelf:
            del mcbShelf[item]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()
