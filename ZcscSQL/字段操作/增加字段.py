

file = 'E:\\WangYulin\\WorkSpace\\数据库更新\\2020数据库更新\\字段相关\\新增字段\\新增-{}-{}.sql'

datalist = [
    {
        'remark': '客户订货单',
        'tablename': 'corder_co',
        'columns': [
            {
                'name': 'da_cid',
                'remark': '送货区域编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'deliveryarea_da',
                'forkey': 'da_cid'
            },
            {
                'name': 'sgs_cid',
                'remark': '签约设计师编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'singnstylist_sgs',
                'forkey': 'sgs_cid'
            },
        ]
    }, {
        'remark': '销售单',
        'tablename': 'sales_ss',
        'columns': [
            {
                'name': 'da_cid',
                'remark': '送货区域编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'deliveryarea_da',
                'forkey': 'da_cid'
            },
        ]
    }, {
        'remark': '销售单子表',
        'tablename': 'salesc_ssc',
        'columns': [
            {
                'name': 'ssc_mshipqty',
                'remark': '送货数量',
                'type': 'decimal(18,5)',
                'isnull': False,
                'default': "0",
                'forkeytab': '',
                'forkey': ''
            },
        ]
    }, {
        'remark': '客户资料',
        'tablename': 'customer_cm',
        'columns': [
            {
                'name': 'da_cid',
                'remark': '送货区域编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'deliveryarea_da',
                'forkey': 'da_cid'
            },
            {
                'name': 'rdl_cid',
                'remark': '项目类型编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'residential_rdl',
                'forkey': 'rdl_cid'
            },
            {
                'name': 'fst_cid',
                'remark': '家具风格编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'furniture_style_fst',
                'forkey': 'fst_cid'
            },
            {
                'name': 'fps_cid',
                'remark': '装修进度编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'fixtures_progress_fps',
                'forkey': 'fps_cid'
            },
        ]
    }, {
        'remark': '意向客户单',
        'tablename': 'cquot_cq',
        'columns': [
            {
                'name': 'da_cid',
                'remark': '送货区域编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'deliveryarea_da',
                'forkey': 'da_cid'
            },
            {
                'name': 'rdl_cid',
                'remark': '项目类型编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'residential_rdl',
                'forkey': 'rdl_cid'
            },
            {
                'name': 'fst_cid',
                'remark': '家具风格编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'furniture_style_fst',
                'forkey': 'fst_cid'
            },
            {
                'name': 'fps_cid',
                'remark': '装修进度编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'fixtures_progress_fps',
                'forkey': 'fps_cid'
            },
            {
                'name': 'sgs_cid',
                'remark': '签约设计师编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'singnstylist_sgs',
                'forkey': 'sgs_cid'
            },
            {
                'name': 'rps_cid',
                'remark': '需求进度编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'require_progress_rps',
                'forkey': 'rps_cid'
            },
        ]
    }, {
        'remark': '客户退货单',
        'tablename': 'crej_cj',
        'columns': [
            {
                'name': 'sgs_cid',
                'remark': '签约设计师编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'singnstylist_sgs',
                'forkey': 'sgs_cid'
            },
        ]
    }, {
        'remark': '客户补货单',
        'tablename': 'cadd_cad',
        'columns': [
            {
                'name': 'da_cid',
                'remark': '送货区域编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'deliveryarea_da',
                'forkey': 'da_cid'
            },
        ]
    }, {
        'remark': '客户订单变更单',
        'tablename': 'corderchangpos_ccs',
        'columns': [
            {
                'name': 'da_cid_old',
                'remark': '原送货区域编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'deliveryarea_da',
                'forkey': 'da_cid'
            },
            {
                'name': 'da_cid_new',
                'remark': '新送货区域编码',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'deliveryarea_da',
                'forkey': 'da_cid'
            },
            {
                'name': 'ccs_csignstylistid_old',
                'remark': '原签约设计师',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': 'singnstylist_sgs',
                'forkey': 'sgs_cid'
            },
        ]
    }, {
        'remark': '条码表',
        'tablename': 'barcode_bc',
        'columns': [
            {
                'name': 'bc_corder',
                'remark': '订单号',
                'type': 'nvarchar(20)',
                'isnull': False,
                'default': "''",
                'forkeytab': '',
                'forkey': ''
            },
            {
                'name': 'bc_iporder',
                'remark': '订单项次',
                'type': 'int',
                'isnull': False,
                'default': "0",
                'forkeytab': '',
                'forkey': ''
            },
        ]
    }, {
        'remark': '产品表',
        'tablename': 'product_pt',
        'columns': [
            {
                'name': 'pt_mpricea',
                'remark': '参考售价A',
                'type': 'decimal(18,5)',
                'isnull': False,
                'default': "0",
                'forkeytab': '',
                'forkey': ''
            },
            {
                'name': 'pt_mpriceb',
                'remark': '参考售价B',
                'type': 'decimal(18,5)',
                'isnull': False,
                'default': "0",
                'forkeytab': '',
                'forkey': ''
            },
            {
                'name': 'pt_mpricec',
                'remark': '参考售价C',
                'type': 'decimal(18,5)',
                'isnull': False,
                'default': "0",
                'forkeytab': '',
                'forkey': ''
            },
            {
                'name': 'pt_mpriced',
                'remark': '参考售价D',
                'type': 'decimal(18,5)',
                'isnull': False,
                'default': "0",
                'forkeytab': '',
                'forkey': ''
            },
            {
                'name': 'pt_mpricee',
                'remark': '参考售价E',
                'type': 'decimal(18,5)',
                'isnull': False,
                'default': "0",
                'forkeytab': '',
                'forkey': ''
            },
            {
                'name': 'pt_mpricef',
                'remark': '参考售价F',
                'type': 'decimal(18,5)',
                'isnull': False,
                'default': "0",
                'forkeytab': '',
                'forkey': ''
            },
        ]
    },{
        'remark': '送货单子表',
        'tablename': 'shipc_sipc',
        'columns': [
            {
                'name': 'sipc_mpayamt',
                'remark': '金额',
                'type': 'decimal(18,5)',
                'isnull': False,
                'default': "0",
                'forkeytab': '',
                'forkey': ''
            },
        ]
    },{
        'remark': '货币资料',
        'tablename': 'syscoin_sc',
        'columns': [
            {
                'name': 'sc_currentRate',
                'remark': '实时汇率',
                'type': 'decimal(18,5)',
                'isnull': False,
                'default': "1",
                'forkeytab': '',
                'forkey': ''
            },
        ]
    },
]

iftemp = """--{}
IF COL_LENGTH('{}','{}') IS NULL
BEGIN
{}
{}{}
PRINT '[{}] 完成'
END
"""

coltemp = "ALTER TABLE {} ADD {} {} {} CONSTRAINT DF_{}_{} DEFAULT {}"
forkeytemp = """ALTER TABLE {}  with check add  constraint [fk_{}_{}] foreign key([{}]) references {} ([{}])
ALTER TABLE {} check constraint [fk_{}_{}]"""
remarktemp = "EXEC sys.sp_addextendedproperty @name=N'MS_Description', @value=N'{}' , \
@level0type=N'SCHEMA',@level0name=N'dbo', @level1type=N'TABLE',@level1name=N'{}', @level2type=N'COLUMN',@level2name=N'{}'"


for item in datalist:
    remarktb = item['remark']
    tablename = item['tablename']
    cols = item['columns']
    index = 1
    sql = '/*\n添加 普通字段\n序号用于快速定位,非正常执行语句\n*/\n'
    sql += "\n--<<{}>>\n".format(remarktb)
    for col in cols:
        name = col['name']
        remark = col['remark']
        typec = col['type']
        default = col['default']
        forkeytab = col['forkeytab']
        forkey = col['forkey']
        if col['isnull'] == True:
            isnull = 'NULL'
        else:
            isnull = 'NOT NULL'
        colsql = coltemp.format(tablename, name, typec,
                                isnull, tablename, name, default)
        forkeysql = ''
        if forkeytab != '':
            forkeysql += '\n' + forkeytemp.format(tablename, tablename, forkeytab,
                                                  name, forkeytab, forkey, tablename, tablename, forkeytab)
        remarksql = remarktemp.format(remark, tablename, name)
        sql += iftemp.format(remark, tablename, name,
                             colsql, remarksql, forkeysql, index)
        index += 1
    filept = file.format(remarktb, tablename)
    with open(filept, 'w', encoding='utf-8-sig') as f:
        f.write(sql)
        print(filept)
