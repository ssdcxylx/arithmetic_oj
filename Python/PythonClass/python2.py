# -*- coding:utf-8 -*-

database = {'张三': {'Java': 99, 'Python': 88}, '李四':  {'Java': 77, 'Python': 66}}

name = input("请输入学生姓名：")
# 判断是否存在的方式
# if name in database:
# 捕获异常的方式
try:
    # 第一种字符串格式化方式
    print('{0}的Java成绩为{1}，Python成绩为{2}'.format(name, database[name]['Java'], database[name]['Python']))
    # 第二种字符串格式化方式
    print('%s的Java成绩为%s，Python成绩为%s' % (name, database[name]['Java'], database[name]['Python']))
    # 第三种字符串格式化方式
    print('{name}的Java成绩为{Java}，Python成绩为{Python}'.format_map({'name': name,
                                                               'Java': database[name]['Java'],
                                                               'Python': database[name]['Python']}))

    # 使用update更新字典
    # 第一种方法
    database.update({name: {'Java': 88, 'Python': 77}})
    print('{0}修改后的Java成绩为{1}，修改后的Python成绩为{2}'.format(name, database[name]['Java'], database[name]['Python']))
    # 第二种方法
    database[name].update({'Java': 77})
    print('{0}修改后的Java成绩为{1}，修改后的Python成绩为{2}'.format(name, database[name]['Java'], database[name]['Python']))
    """
    # 错误的例子（会将整个key为name的字典替换掉）
    database.update({'张三': {'Java': 77}})
    print(database) # 输出为{'张三': {'Java': 77}, '李四': {'Java': 77, 'Python': 66}}
    """
except KeyError:
    print("异常：未查询到学生%s" % name)
    print(database)
