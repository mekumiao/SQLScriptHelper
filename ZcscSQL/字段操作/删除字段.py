
file = 'E:\\WangYulin\\WorkSpace\\数据库更新\\2020数据库更新\\字段相关\\删除字段\\删除-{}-{}.sql'


datalist = [{
    'remark': '销售单子表',
    'tablename': 'salesc_ssc',
    'columns': [
        {
            'name': 'ssc_mshipqty',
            'remark': '送货数量',
            'isdefault': True,
            'forkeytab': '',
            'forkey': ''
        },
    ]
}, ]

iftemp = """IF COL_LENGTH('salesc_ssc','ssc_mshipqty') IS NOT NULL
BEGIN
{}PRINT '[{}] 完成'
END
"""

dropctemp = 'ALTER TABLE {} DROP CONSTRAINT {}\n'
droptbtemp = 'ALTER TABLE {} DROP COLUMN {}\n'

for item in datalist:
    remark = item['remark']
    tablename = item['tablename']
    index = 1
    sql = '/*\n删除 普通字段\n序号用于快速定位,非正常执行语句\n*/\n'
    sql += "\n--<<{}>>\n".format(remark)
    for col in item['columns']:
        name = col['name']
        rek = col['remark']
        isdefault = col['isdefault']
        forkeytab = col['forkeytab']
        forkey = col['forkey']
        colstr = ''
        if isdefault:
            df = 'DF_{}_{}'.format(tablename, name)
            colstr += dropctemp.format(tablename, df)
        if forkeytab != '':
            fk = 'FK_{}_{}'.format(tablename, name)
            colstr += dropctemp.format(tablename, fk)
        colstr += droptbtemp.format(tablename, name)
        sql += iftemp.format(colstr, index)
        index += 1
    filept = file.format(remark, tablename)
    with open(filept, 'w', encoding='utf-8-sig') as f:
        f.write(sql)
        print(filept)
