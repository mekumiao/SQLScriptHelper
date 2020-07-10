#
# 修改页面配置字段
# #
# {
#     'name': '拆货单',
#     'pld_cid': '2A',
#     'pl_clevel': '0548',
#     'pyt_cpropertyset': 'v_assemInfo',
#     'pytc_cename': ['am_beginmanname', ]
# },

filepath = 'E:\\WangYulin\\WorkSpace\\数据库更新\\2020数据库更新\\导航、区域、权限\\自动生成\\修改页面设置.sql'

strwhere = [{
    'name': '报废单',
    'pld_cid': '2A',
    'pl_clevel': '0564',
    'pyt_cpropertyset': 'v_scrapInfo',
    'pytc_cename': ['srp_cbeginmanname', 'srp_ceditmanname', 'srp_cmtmanname', ]
}, {
    'name': '还货单',
    'pld_cid': '2A',
    'pl_clevel': '0520',
    'pyt_cpropertyset': 'v_backtrackInfo',
    'pytc_cename': ['bak_cbeginmanname', 'bak_ceditmanname', 'bak_cmtmanname', ]
}, {
    'name': '借货单',
    'pld_cid': '2A',
    'pl_clevel': '0519',
    'pyt_cpropertyset': 'v_loanInfo',
    'pytc_cename': ['lo_cbeginmanname', 'lo_ceditmanname', 'lo_cmtmanname', ]
}, {
    'name': '补货单',
    'pld_cid': '2A',
    'pl_clevel': '0415',
    'pyt_cpropertyset': 'v_caddInfo',
    'pytc_cename': ['cad_cbeginmanname', 'cad_ceditmanname', 'cad_cmtmanname', ]
}, {
    'name': '退货单',
    'pld_cid': '2A',
    'pl_clevel': '0414',
    'pyt_cpropertyset': 'v_crejInfo',
    'pytc_cename': ['cj_cmtmanname', 'cj_ceditmanname', 'cj_cbeginmanname', ]
}, {
    'name': '送修单',
    'pld_cid': '2A',
    'pl_clevel': '0567',
    'pyt_cpropertyset': 'v_repairInfo',
    'pytc_cename': ['ra_cbeginmanname', 'ra_ceditmanname', 'ra_cmtmanname', ]
}, {
    'name': '质量检验单',
    'pld_cid': '2A',
    'pl_clevel': '0561',
    'pyt_cpropertyset': 'v_quality_checkInfo',
    'pytc_cename': ['qc_cbeginmanname', 'qc_ceditmanname', 'qc_cmtmanname', ]
}, {
    'name': '成本调整单',
    'pld_cid': '2A',
    'pl_clevel': '0551',
    'pyt_cpropertyset': 'v_prodcost_changeInfo',
    'pytc_cename': ['pg_cbeginmanname', 'pg_ceditmanname', 'pg_cmtmanname', ]
}, ]

remark = ['建立人名称', '修改人名称', '审核（反审）人名称']
# like = ['创建%人', '建立%人', '修改%人', '编辑%人', '审核%人',
# '建立日期','创建日期','修改日期','编辑日期','审核%日期','建档日期',
# '建立时间','创建时间','修改时间','编辑时间','审核%时间',
# ]

# 名称
name = ['beginmanname', 'editmanname', 'mtmanname',
        'begindt', 'editdt', 'cmtdt', 'auditflag', 'cmtflag', 'dmtdt']
# 编码
code = ['beginman', 'editman', 'cmtman']

iftemp = "if not exists(select * from propertysetc_pytc where pl_clevel='{}' and pld_cid='{}' and pytc_cename='{}')\nbegin\n\t{}\n\t{}\n\tprint '[{}]完成'\nend\n"
iitemtemp = "select @iitem=max(pytc_iitem)+1 from propertysetc_pytc where pl_clevel='{}' and pld_cid='{}'"
inserttemp = "insert propertysetc_pytc values('admin','{}','{}','{}','{}','{}',@iitem,'','String',100,'0','0','0','','03','','billstatus','','{}')"
updatetemp = "update propertysetc_pytc set pytc_cremark='billstatus' where pl_clevel='{}' and pld_cid='{}' and ({})"
notupdatetemp = "update propertysetc_pytc set pytc_cremark='' where pl_clevel='{}' and pld_cid='{}' and ({})"
nameliketemp = "pytc_cename like '%{}%'"
codeliketemp = "pytc_cename like '%{}'"
selecttemp = "select * from propertysetc_pytc where pl_clevel='{}' and pld_cid='{}' and ({})"
trantemp = """/*
修改 或 新增 建立人名称 修改人名称 审核人名称
*/
begin try
begin tran

declare @iitem int --序号
{}
commit tran
end try
begin catch
rollback tran
end catch
"""

sql = ''
index = 1

for item in strwhere:
    sql += '\n--{}\n'.format(item['name'])
    for inx, cename in enumerate(item['pytc_cename']):
        pl_clevel = item['pl_clevel']
        pld_cid = item['pld_cid']
        pyt_cpropertyset = item['pyt_cpropertyset']

        selsql = iitemtemp.format(pl_clevel, pld_cid)
        inssql = inserttemp.format(
            pl_clevel, pld_cid, pyt_cpropertyset, cename, remark[inx], remark[inx])
        ifsql = iftemp.format(pl_clevel, pld_cid, cename,
                              selsql, inssql, index)
        sql += ifsql
        index += 1

sql += '\n\n--修改 页面设置中 建立人 修改人 审核人...的显示'
namesql = ' or '.join([nameliketemp.format(item) for item in name])
codesql = ' or '.join([codeliketemp.format(item) for item in code])
for item in strwhere:
    pl_clevel = item['pl_clevel']
    pld_cid = item['pld_cid']

    updsql = '\n' + updatetemp.format(pl_clevel, pld_cid, namesql) + \
        '\n' + notupdatetemp.format(pl_clevel, pld_cid, codesql)
    sql += updsql + '\n'

transql = trantemp.format(sql)

for item in strwhere:
    name = item['name']
    pl_clevel = item['pl_clevel']
    pld_cid = item['pld_cid']

    selsql = '\n--{}\n--'.format(name) + selecttemp.format(pl_clevel, pld_cid, namesql) + \
        '\n--' + selecttemp.format(pl_clevel, pld_cid, codesql)
    transql += selsql + '\n'

with open(filepath, 'w') as f:
    f.write(transql)
