#
# 自动生成权限 sql脚本
# #

file = 'E:\\WangYulin\\WorkSpace\\数据库更新\\2020数据库更新\\导航、区域、权限\\自动生成\\权限.sql'

common = [
    {
        'pl_cpopeid': 'Q',
        'pl_cfuncdes': '查询',
        'pl_capiname': '',
    },
    {
        'pl_cpopeid': 'I',
        'pl_cfuncdes': '新增',
        'pl_capiname': '',
    },
    {
        'pl_cpopeid': 'U',
        'pl_cfuncdes': '修改',
        'pl_capiname': '',
    },
    {
        'pl_cpopeid': 'D',
        'pl_cfuncdes': '删除',
        'pl_capiname': '',
    },
    {
        'pl_cpopeid': 'C',
        'pl_cfuncdes': '复制',
        'pl_capiname': '',
    },
    {
        'pl_cpopeid': 'P',
        'pl_cfuncdes': '打印',
        'pl_capiname': '',
    },
    {
        'pl_cpopeid': 'E',
        'pl_cfuncdes': '审核',
        'pl_capiname': '',
    },
    {
        'pl_cpopeid': 'H',
        'pl_cfuncdes': '弃审',
        'pl_capiname': '',
    },
]

#
# 设置权限apis
# ##
authlist = [
    {
        'pl_clevel': '0418',
        'pl_cfuncdes': '送货单',
        'query_clevel': '0419',
        'query_cfuncdes': '送货单查询',
        'apis': [
            'ShipService/SearchShipByView',
            'ShipService/CreateShipSpcByView',
            'ShipService/UpdateShipSpcByView',
            'ShipService/DeleteShipByView',
            '',
            '',
            'ShipService/AuthShip',
            'ShipService/UnAuthShip',
        ],
        'child': []
    },{
        'pl_clevel': '0115',
        'pl_cfuncdes': '系统日志',
        'query_clevel': '0115',
        'query_cfuncdes': '系统日志查询',
        'apis': [
            'SysLogService/SearchSyslog',
            '',
            '',
            'SysLogService/DeleteSyslog',
            '',
            '',
            '',
            '',
        ],
        'child': []
    }
]


iftemp = "if not exists(select * from popelist_pl where pl_clevel='{}')\n"
instemp = """begin
insert into popelist_pl values ('{}','{}','{}','{}')
print '[{}] 完成'
end
"""

sql = '/*\n序号用于快速定位,非正常执行语句\n*/\n'
index = 1

for item in authlist:
    sql += '\n--{}\n'.format(item['pl_cfuncdes'])
    sql += iftemp.format(item['pl_clevel'])
    sql += instemp.format(item['pl_clevel'], '',
                          item['pl_cfuncdes'], '', index)
    index += 1
    for i in range(len(item['apis'])):
        level = item['pl_clevel'] + str(i+1).rjust(2, '0')
        sql += iftemp.format(level)
        sql += instemp.format(level, common[i]
                              ['pl_cpopeid'], common[i]['pl_cfuncdes'], item['apis'][i], index)
        index += 1
    sql += iftemp.format(item['query_clevel'])
    sql += instemp.format(item['query_clevel'], '',
                          item['query_cfuncdes'], '', index)
    index += 1

with open(file, 'w') as f:
    f.write(sql)
