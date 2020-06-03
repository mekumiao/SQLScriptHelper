#
# 控制生成SQL
# #
from scriptToJson import GetJson
from createTabSQL import GetTabSQL
import json
import os

# json输出目录
jsonoutpath = 'E:\\WangYulin\\WorkSpace\\数据库更新\\2020数据库更新\\SQLScript\\JSON\\'
# sql输出目录
taboutpath = 'E:\\WangYulin\\WorkSpace\\数据库更新\\2020数据库更新\\表相关\\'
# 脚本路径
scriptpath = 'E:\\WangYulin\\WorkSpace\\数据库更新\\2020数据库更新\\SQLScript\\{}.txt'

# 需要执行的脚本名称
jsonpath = R'E:\WangYulin\WorkSpace\数据库更新\2020数据库更新\SQLScript\tabset.json'
with open(jsonpath, 'r', encoding='utf8') as f:
    jsonstr = f.read()
    paths = json.loads(jsonstr)

for name in paths:
    # 脚本路径
    path = scriptpath.format(name)
    if os.path.exists(path):
        # 获取json
        jsonfile = GetJson(jsonoutpath, path)
        # 生成sql
        sqlfile = GetTabSQL(taboutpath, jsonfile)
        print('生成成功:' + sqlfile)
    else:
        print('路径不存在:' + path)
