
def saveTool(func):
    """
    保存联系人装饰器
    保存到当前目录 名为 contacts.txt 文件下
    如果想要自定义文件名需要传入 file 参数，即 file="xxx"
    """
    from functools import wraps
    from os.path import exists
    @wraps(func)
    def inner(*args, **kwargs):
        fileName = kwargs.get("file", "contacts") + '.txt'
        if not exists(fileName):
            print("检测到没有联系人文件，正在创建……")
            f = open(fileName, 'w', encoding='utf-8')
            f.write("# 联系人和号码要用两个空格隔开，如下\n# 张三  19756438368")
            f.close()
            print("联系人文件创建完毕\n")
        else:
            print("已有联系人文件，读取中……")
        global contacts
        contacts = {
            friend.split("  ")[0]: friend.split("  ")[1]
            for friend in open(fileName, encoding='utf-8', mode='r') if not friend.startswith("#") and friend.strip()
        }
        print("开始执行您的程序……\n")
        func(contacts=contacts, *args, **kwargs)
        print("\n您的程序执行完毕")
        print("\n保存联系人中……")
        with open(fileName, 'w', encoding='utf-8') as f:
            f.write("# 联系人和号码要用两个空格隔开，如下\n# 张三  19756438368\n")
            for item in contacts:
                if item and contacts[item]:
                    f.write(f"\n{item}  {contacts[item]}")
        print("联系人保存完毕")
    return inner
