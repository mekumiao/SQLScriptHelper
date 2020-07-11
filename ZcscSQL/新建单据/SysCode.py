
file = 'E:\\WangYulin\\WorkSpace\\数据库更新\\2020数据库更新\\导航、区域、权限\\自动生成\\SysCode.sql'

codelist = [
    {
        'remark': '送货单',
        'sd_clevel': '0418',
        'sd_cpreflag': 'SIP',
    },
]

iftemp = "if not exists(select * from syscode_sd where sd_clevel='{}')"
instltemp = """begin
insert syscode_sd values('','{}','1','1','{}','{}YYYMMDDSSSSS',5,'y','1','1','1',4,2,2,1,'0','0','0','0')
print '[{}] 完成'
end
"""

sql = '/*\n序号用于快速定位,非正常执行语句\n*/\n'
index = 1

for item in codelist:
    sql += '\n--{}\n'.format(item['remark'])
    sql += iftemp.format(item['sd_clevel'])
    sql += instltemp.format(item['sd_clevel'],
                            item['sd_cpreflag'], item['sd_cpreflag'], index)
with open(file, 'w') as f:
    f.write(sql)
