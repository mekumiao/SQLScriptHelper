#
# 生成表SQL
# #
import json


def GetFkName(FKlist, FKname) -> str:
    name = FKname
    for i in range(1, 100):
        if (name in FKlist):
            name = FKname + str(i)
        else:
            FKlist.append(name)
            break
    return name


# 输入输出目录，表信息json。输出表sql文件地址
def GetTabSQL(taboutpath, jsonpath) -> str:
    taboutpath += '{}-{}.sql'
    jsonstr = str

    with open(jsonpath, 'r', encoding='utf8') as f:
        jsonstr = f.read()

    data = json.loads(jsonstr)

    # 删除表模板
    sqldroptemp = """/*
!!
*/
if exists(select * from sys.tables where [name]='{}')
drop table {}
"""
    # 表注释模板
    tabremarktemp = "-- {} {}"
    # 主体模板
    sqlbodytemp = "create table [dbo].[{}](\n{}{}\n)on [primary]\ngo\n"
    # 主键模板
    sqlpktemp = """ constraint [pk_{}] primary key clustered \n(\n{}\n)
with (pad_index = off, statistics_norecompute = off, ignore_dup_key = off, allow_row_locks = on, allow_page_locks = on) on [primary]"""
    # 默认约束模板
    sqldeftemp = "alter table [dbo].[{}] add  constraint [df_{}_{}]  default ({}) for [{}]\ngo\n"
    # 外键约束模板
    sqlforkeytemp = """alter table [dbo].[{}]  with check add  constraint [fk_{}_{}] foreign key([{}])
references [dbo].[{}] ([{}])
go
alter table [dbo].[{}] check constraint [fk_{}_{}]
go\n"""
    # 字段描述模板
    sqldesttemp = """exec sys.sp_addextendedproperty @name=N'MS_Description', @value=N'{}' , @level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'{}', @level2type=N'COLUMN',@level2name=N'{}'
go\n"""

    tabDest = data['tabDest']  # 表描述
    tabName = data['tabName']  # 表名

    # 表注释
    tabremark = tabremarktemp.format(tabDest, tabName)

    # 删除表语句
    sqldrop = sqldroptemp.format(tabName, tabName)

    sqlbody = ''  # 主体语句
    fields = data['tabFields']  # 表字段
    sqlfds = ''  # 字段语句
    for item in fields:
        name = item['name']
        fdtype = item['fdtype']
        isnull = 'null' if item['isnull'] else 'not null'
        sqlfds += "\t[{}] {} {},\n".format(name, fdtype, isnull)

    # 主键语句
    sqlpk = ''
    for item in fields:
        if item['ispk']:
            name = item['name']
            sqlpk += "\t[{}] asc,\n".format(name)
    sqlpks = sqlpktemp.format(tabName, sqlpk[:-2])

    sqlbody += sqlbodytemp.format(tabName, sqlfds, sqlpks)

    # 默认约束语句
    sqldef = ''
    for item in fields:
        name = item['name']
        defval = item['defval']
        if defval != "":
            sqldef += sqldeftemp.format(tabName, tabName, name, defval, name)

    # 外键基表集合,防止重复
    FKlist = []
    # 外键约束语句
    sqlforkey = ''
    for item in fields:
        name = item['name']
        forkeytab = item['forkeytab']
        forkeyfd = item['forkeyfd']
        if forkeytab != "":
            # 防止外键名称重复
            fkeycname = GetFkName(FKlist, forkeytab)
            sqlforkey += sqlforkeytemp.format(tabName, tabName, fkeycname,
                                              name, forkeytab, forkeyfd, tabName, tabName, fkeycname)

    # 字段描述语句
    sqldest = ''
    for item in fields:
        name = item['name']
        dest = item['dest']
        if dest != "":
            sqldest += sqldesttemp.format(dest, tabName, name)

    sql = "{}\n{}\n{}\n{}\n{}\n{}".format(
        sqldrop, tabremark, sqlbody, sqldef, sqlforkey, sqldest)

    with open(taboutpath.format(tabDest, tabName), 'w') as f:
        f.write(sql)
    return taboutpath.format(tabDest, tabName)
