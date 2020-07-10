#
# 用于自动生成 导航.sql
# #

file = 'E:\\WangYulin\\WorkSpace\\数据库更新\\2020数据库更新\\导航、区域、权限\\自动生成\\导航.sql'

funlist = [
    {
        'fl_clevel': '0414',
        'fl_cfuncdes': '客户退货单',
    },
    {
        'fl_clevel': '0422',
        'fl_cfuncdes': '客户退货单查询',
    },
    {
        'fl_clevel': '0415',
        'fl_cfuncdes': '客户补货单',
    },
    {
        'fl_clevel': '0423',
        'fl_cfuncdes': '客户补货单查询',
    },
    {
        'fl_clevel': '0519',
        'fl_cfuncdes': '借货单',
    },
     {
        'fl_clevel': '0522',
        'fl_cfuncdes': '借货单查询',
    },
    {
        'fl_clevel': '0520',
        'fl_cfuncdes': '还货单',
    },
    {
        'fl_clevel': '0523',
        'fl_cfuncdes': '还货单查询',
    },
    {
        'fl_clevel': '0548',
        'fl_cfuncdes': '拆并历史',
    },
    {
        'fl_clevel': '0554',
        'fl_cfuncdes': '拆并历史查询',
    },
    {
        'fl_clevel': '0551',
        'fl_cfuncdes': '成本调整单',
    },
    {
        'fl_clevel': '0552',
        'fl_cfuncdes': '成本调整单查询',
    },
    {
        'fl_clevel': '0561',
        'fl_cfuncdes': '质量检验单',
    },
    {
        'fl_clevel': '0562',
        'fl_cfuncdes': '质量检验单查询',
    },{
        'fl_clevel': '0564',
        'fl_cfuncdes': '报废单',
    },
    {
        'fl_clevel': '0565',
        'fl_cfuncdes': '报废单查询',
    },{
        'fl_clevel': '0567',
        'fl_cfuncdes': '送修单',
    },
    {
        'fl_clevel': '0568',
        'fl_cfuncdes': '送修单查询',
    },
    {
        'fl_clevel': '0360',
        'fl_cfuncdes': '安全库存设定查询',
    },
    {
        'fl_clevel': '0342',
        'fl_cfuncdes': '应付款账龄分析表',
    },{
        'fl_clevel': '0250',
        'fl_cfuncdes': '送货区域',
    },{
        'fl_clevel': '0251',
        'fl_cfuncdes': '签约设计师',
    },{
        'fl_clevel': '0252',
        'fl_cfuncdes': '项目类型',
    },{
        'fl_clevel': '0253',
        'fl_cfuncdes': '家具风格',
    },{
        'fl_clevel': '0254',
        'fl_cfuncdes': '装修进度',
    },{
        'fl_clevel': '0255',
        'fl_cfuncdes': '需求进度',
    },{
        'fl_clevel': '0256',
        'fl_cfuncdes': '备注',
    },{
        'fl_clevel': '0257',
        'fl_cfuncdes': '商品库存属性',
    },{
        'fl_clevel': '0271',
        'fl_cfuncdes': '厂家资料导入',
    },{
        'fl_clevel': '0272',
        'fl_cfuncdes': '客户资料导入',
    },{
        'fl_clevel': '0273',
        'fl_cfuncdes': '颜色资料导入',
    },{
        'fl_clevel': '0535',
        'fl_cfuncdes': '期初资料',
    },{
        'fl_clevel': '0537',
        'fl_cfuncdes': '期间重算',
    },
]

iftemp = "\nif (not exists(select * from funclist_fl where fl_clevel='{}'))"
begintemp = "\nbegin\n{}\nprint '[{}] 完成'\nend"
inserttmep = "insert funclist_fl(fl_cmodeid,fl_clevel,fl_cfuncdes,fl_cchkinit) values('','{}','{}',0)"

sql = '/*\n序号用于快速定位,非正常执行语句\n*/'
index = 1

for item in funlist:
    fl_clevel = item['fl_clevel']
    fl_cfuncdes = item['fl_cfuncdes']
    sqlif = iftemp.format(fl_clevel)
    sqlin = inserttmep.format(fl_clevel, fl_cfuncdes)
    sqlbegin = begintemp.format(sqlin, index)
    sql += sqlif + sqlbegin
    index += 1

with open(file, 'w') as f:
    f.write(sql)
