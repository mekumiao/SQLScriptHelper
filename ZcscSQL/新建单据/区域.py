#
# 自动生成区域 sql脚本
# #

file = 'E:\\WangYulin\\WorkSpace\\数据库更新\\2020数据库更新\\导航、区域、权限\\自动生成\\区域.sql'

oaalist = [
    {
        'remake': '客户退货单',
        'data': [{
            'oaa_cid': 'v_crejInfo',
            'oaa_cname': '客户退货单主表',
            'oaa_capi': 'CrejService/SearchCrejByView',
            'oaa_cremake': '客户退货单'
        },
            {
            'oaa_cid': 'v_crejcInfo',
            'oaa_cname': '客户退货单子表',
            'oaa_capi': 'CrejService/SearchCrejcByView',
            'oaa_cremake': '客户退货单'
        },
            {
            'oaa_cid': 'v_crejMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'CrejService/SearchCrejAllByView',
            'oaa_cremake': '客户退货单'
        },
            {
            'oaa_cid': 'v_crejInfoSum',
            'oaa_cname': '全表汇总',
            'oaa_capi': 'CrejService/GetCrejInfoSum',
            'oaa_cremake': '客户退货单'
        },
        ]
    },
    {
        'remake': '客户补货单',
        'data': [{
            'oaa_cid': 'v_caddInfo',
            'oaa_cname': '客户补货单主表',
            'oaa_capi': 'CaddService/SearchCaddByView',
            'oaa_cremake': '客户补货单'
        },
            {
            'oaa_cid': 'v_caddcInfo',
            'oaa_cname': '客户补货单子表',
            'oaa_capi': 'CaddService/SearchCaddcByView',
            'oaa_cremake': '客户补货单'
        }, {
            'oaa_cid': 'v_caddMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'CaddService/SearchCaddAllByView',
            'oaa_cremake': '客户补货单'
        },
            {
            'oaa_cid': 'v_caddInfoSum',
            'oaa_cname': '全表汇总',
            'oaa_capi': 'CaddService/GetCaddInfoSum',
            'oaa_cremake': '客户补货单'
        }, ]
    },
    {
        'remake': '客户退货单-相关单号',
        'data': [{
            'oaa_cid': 'v_crejForSalesView',
            'oaa_cname': '客户订单已销资料',
            'oaa_capi': 'CrejService/SearchForSalesView',
            'oaa_cremake': '客户退货单'
        },
            {
            'oaa_cid': 'v_crejForSalescView1',
            'oaa_cname': '客户订单已销-未送-商品',
            'oaa_capi': 'CrejService/SearchForSalescView1',
            'oaa_cremake': '客户退货单'
        },
            {
            'oaa_cid': 'v_crejForSalescView2',
            'oaa_cname': '客户订单已销-已送-商品',
            'oaa_capi': 'CrejService/SearchForSalescView2',
            'oaa_cremake': '客户退货单'
        },
            {
            'oaa_cid': 'v_crejForSalesAllView',
            'oaa_cname': '销售单资料',
            'oaa_capi': 'CrejService/SearchSalesAllView',
            'oaa_cremake': '客户退货单'
        },
            {
            'oaa_cid': 'v_crejForOrderView',
            'oaa_cname': '客户订单未销资料',
            'oaa_capi': 'CrejService/SearchForOrderView',
            'oaa_cremake': '客户退货单'
        },
            {
            'oaa_cid': 'v_crejForOrdercView',
            'oaa_cname': '客户订单未销商品',
            'oaa_capi': 'CrejService/SearchForOrdercView',
            'oaa_cremake': '客户退货单'
        },
            {
            'oaa_cid': 'v_crejForCaddView',
            'oaa_cname': '客户补货单资料',
            'oaa_capi': 'CrejService/SearchForCaddView',
            'oaa_cremake': '客户退货单'
        },
            {
            'oaa_cid': 'v_crejForCaddcView',
            'oaa_cname': '客户补货单商品',
            'oaa_capi': 'CrejService/SearchForCaddcView',
            'oaa_cremake': '客户退货单'
        }, ]
    },
    {
        'remake': '客户补货单-相关单号',
        'data': [{
            'oaa_cid': 'v_crejMakeInfoAll',
            'oaa_cname': '退后补货-退货单资料',
            'oaa_capi': 'CrejService/SearchCrejAllByView',
            'oaa_cremake': '客户补货单'
        },
            {
            'oaa_cid': 'v_caddForOrderView',
            'oaa_cname': '销售加单-订货单资料',
            'oaa_capi': 'CaddService/SearchForOrderView',
            'oaa_cremake': '客户补货单'
        }, ]
    },
    {
        'remake': '借货单',
        'data': [{
            'oaa_cid': 'v_loanInfo',
            'oaa_cname': '借货单主表',
            'oaa_capi': 'LoanService/SearchLoanByView',
            'oaa_cremake': '借货单'
        },
            {
            'oaa_cid': 'v_loancInfo',
            'oaa_cname': '借货单子表',
            'oaa_capi': 'LoanService/SearchLoancByView',
            'oaa_cremake': '借货单'
        }, {
            'oaa_cid': 'v_loanMan',
            'oaa_cname': '借货人资料',
            'oaa_capi': 'LoanService/SearchLoanManByView',
            'oaa_cremake': '借货单'
        }, {
            'oaa_cid': 'v_loanMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'LoanService/SearchLoanAllByView',
            'oaa_cremake': '借货单'
        },
            {
            'oaa_cid': 'v_loanInfoSum',
            'oaa_cname': '全表汇总',
            'oaa_capi': 'LoanService/GetLoanInfoSum',
            'oaa_cremake': '借货单'
        }, ]
    },
    {
        'remake': '还货单',
        'data': [{
            'oaa_cid': 'v_backtrackInfo',
            'oaa_cname': '还货单主表',
            'oaa_capi': 'BacktrackService/SearchBacktrackByView',
            'oaa_cremake': '还货单'
        }, {
            'oaa_cid': 'v_backtrackcInfo',
            'oaa_cname': '还货单子表',
            'oaa_capi': 'BacktrackService/SearchBacktrackcByView',
            'oaa_cremake': '还货单'
        },
            {
            'oaa_cid': 'v_backtrackMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'BacktrackService/SearchBacktrackAllByView',
            'oaa_cremake': '还货单'
        },
            {
            'oaa_cid': 'v_backtrackInfoSum',
            'oaa_cname': '全表汇总',
            'oaa_capi': 'BacktrackService/GetBacktrackInfoSum',
            'oaa_cremake': '还货单'
        }]
    },
    {
        'remake': '拆并历史',
        'data': [{
            'oaa_cid': 'v_assemInfo',
            'oaa_cname': '拆并历史主表',
            'oaa_capi': 'AssemService/SearchAessemByView',
            'oaa_cremake': '拆并历史'
        }, {
            'oaa_cid': 'v_assemcInfo',
            'oaa_cname': '拆并历史子表',
            'oaa_capi': 'AssemService/SearchAssemcByView',
            'oaa_cremake': '拆并历史'
        }, {
            'oaa_cid': 'v_assemMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'AssemService/SearchAssemAllByView',
            'oaa_cremake': '拆并历史'
        }, {
            'oaa_cid': 'v_assemInfoSum',
            'oaa_cname': '全表汇总',
            'oaa_capi': 'AssemService/GetAssemInfoSum',
            'oaa_cremake': '拆并历史'
        }, ]
    },
    {
        'remake': '成本调整单',
        'data': [{
            'oaa_cid': 'v_prodcost_changeInfo',
            'oaa_cname': '成本调整单主表',
            'oaa_capi': 'ProdcostService/SearchProdcostChangeByView',
            'oaa_cremake': '成本调整单'
        }, {
            'oaa_cid': 'v_prodcost_changecInfo',
            'oaa_cname': '成本调整单子表',
            'oaa_capi': 'ProdcostService/SearchProdcostChangecByView',
            'oaa_cremake': '成本调整单'
        }, {
            'oaa_cid': 'v_prodcost_changeMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'ProdcostService/SearchProdcostChangeAllByView',
            'oaa_cremake': '成本调整单'
        }, {
            'oaa_cid': 'v_prodcost_changeInfoSum',
            'oaa_cname': '全表汇总',
            'oaa_capi': 'ProdcostService/GetProdcostChangeInfoSum',
            'oaa_cremake': '成本调整单'
        }, {
            'oaa_cid': 'v_stockcForoutins',
            'oaa_cname': '库存资料',
            'oaa_capi': 'ProdcostService/SearchStockcForOutins',
            'oaa_cremake': '成本调整单'
        }, ]
    },
    {
        'remake': '质量检验单',
        'data': [{
            'oaa_cid': 'v_quality_checkInfo',
            'oaa_cname': '质量检验单主表',
            'oaa_capi': 'QualityService/SearchQualityByView',
            'oaa_cremake': '质量检验单'
        }, {
            'oaa_cid': 'v_quality_checkcInfo',
            'oaa_cname': '质量检验单子表',
            'oaa_capi': 'QualityService/SearchQualitycByView',
            'oaa_cremake': '质量检验单'
        }, {
            'oaa_cid': 'v_quality_checkcMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'QualityService/SearchQualityAllByView',
            'oaa_cremake': '质量检验单'
        }, {
            'oaa_cid': 'v_quality_checkInfoSum',
            'oaa_cname': '全表汇总',
            'oaa_capi': 'QualityService/GetQualityInfoSum',
            'oaa_cremake': '质量检验单'
        }, {
            'oaa_cid': 'v_vorderForOrderInfo',
            'oaa_cname': '指定采购订单资料',
            'oaa_capi': 'QualityService/SearchVorderForOrderVew',
            'oaa_cremake': '质量检验单'
        }]
    }, {
        'remake': '报废单',
        'data': [{
            'oaa_cid': 'v_scrapInfo',
            'oaa_cname': '报废单主表',
            'oaa_capi': 'ScrapService/SearchScrapByView',
            'oaa_cremake': '报废单'
        }, {
            'oaa_cid': 'v_scrapcInfo',
            'oaa_cname': '报废单子表',
            'oaa_capi': 'ScrapService/SearchScrapcByView',
            'oaa_cremake': '报废单'
        }, {
            'oaa_cid': 'v_scrapMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'ScrapService/SearchScrapAllByView',
            'oaa_cremake': '报废单'
        }, {
            'oaa_cid': 'v_scrapInfoSum',
            'oaa_cname': '全表汇总',
            'oaa_capi': 'ScrapService/GetScrapInfoSum',
            'oaa_cremake': '报废单'
        }]
    }, {
        'remake': '送修单',
        'data': [{
            'oaa_cid': 'v_repairInfo',
            'oaa_cname': '送修单主表',
            'oaa_capi': 'RepairService/SearchRepairByView',
            'oaa_cremake': '送修单'
        }, {
            'oaa_cid': 'v_repaircInfo',
            'oaa_cname': '送修单子表',
            'oaa_capi': 'RepairService/SearchRepaircByView',
            'oaa_cremake': '送修单'
        }, {
            'oaa_cid': 'v_repairMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'RepairService/SearchRepairAllByView',
            'oaa_cremake': '送修单'
        }, {
            'oaa_cid': 'v_repairInfoSum',
            'oaa_cname': '全表汇总',
            'oaa_capi': 'RepairService/GetRepairInfoSum',
            'oaa_cremake': '送修单'
        }]
    }, {
        'remake': '商品安全库存设定',
        'data': [{
            'oaa_cid': 'v_prodsafeMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'ProdsafeService/SearchProdsafeAllByView',
            'oaa_cremake': '商品安全库存设定'
        }]
    }, {
        'remake': '应付款账龄分析表',
        'data': [{
            'oaa_cid': 'DTO_yfzk',
            'oaa_cname': '应付款账龄分析表',
            'oaa_capi': 'YFKZLService/SearchYfkzlByView',
            'oaa_cremake': '应付款账龄分析表'
        }]
    }, {
        'remake': '送货区域',
        'data': [{
            'oaa_cid': 'deliveryarea_da',
            'oaa_cname': '送货区域',
            'oaa_capi': 'DeliveryareaService/SearchDeliveryarea',
            'oaa_cremake': '送货区域'
        }, ]
    }, {
        'remake': '签约设计师',
        'data': [{
            'oaa_cid': 'v_singnstylistInfo',
            'oaa_cname': '签约设计师',
            'oaa_capi': 'SingnstylistService/SearchSingnstylist',
            'oaa_cremake': '签约设计师'
        }, ]
    }, {
        'remake': '项目类型',
        'data': [{
            'oaa_cid': 'residential_rdl',
            'oaa_cname': '项目类型',
            'oaa_capi': 'ResidentialService/SearchResidential',
            'oaa_cremake': '项目类型'
        }, ]
    }, {
        'remake': '家具风格',
        'data': [{
            'oaa_cid': 'furniture_style_fst',
            'oaa_cname': '家具风格',
            'oaa_capi': 'FurnitureService/SearchFurniture',
            'oaa_cremake': '家具风格'
        }, ]
    }, {
        'remake': '装修进度',
        'data': [{
            'oaa_cid': 'fixtures_progress_fps',
            'oaa_cname': '装修进度',
            'oaa_capi': 'FixturesService/SearchFixtures',
            'oaa_cremake': '装修进度'
        }, ]
    }, {
        'remake': '需求进度',
        'data': [{
            'oaa_cid': 'require_progress_rps',
            'oaa_cname': '需求进度',
            'oaa_capi': 'RequireService/SearchRequire',
            'oaa_cremake': '需求进度'
        }, ]
    }, {
        'remake': '备注',
        'data': [{
            'oaa_cid': 'v_remarkInfo',
            'oaa_cname': '备注',
            'oaa_capi': 'RemarkService/SearchRemark',
            'oaa_cremake': '备注'
        }, ]
    }, {
        'remake': '商品库存属性',
        'data': [{
            'oaa_cid': 'v_warehousattrInfo',
            'oaa_cname': '商品库存属性',
            'oaa_capi': 'WarehousattrService/SearchWarehousattr',
            'oaa_cremake': '商品库存属性'
        }, ]
    }, {
        'remake': '厂家资料导入',
        'data': [{
            'oaa_cid': 'v_vendor_impInfo',
            'oaa_cname': '查询主表',
            'oaa_capi': 'VendorImpService/SearchVendorImpByView',
            'oaa_cremake': '厂家资料导入'
        }, {
            'oaa_cid': 'vendorc_imp_vmpc',
            'oaa_cname': '查询子表',
            'oaa_capi': 'VendorImpService/SearchVendorImpcByView',
            'oaa_cremake': '厂家资料导入'
        }, ]
    }, {
        'remake': '客户资料导入',
        'data': [{
            'oaa_cid': 'v_customer_impInfo',
            'oaa_cname': '查询主表',
            'oaa_capi': 'CustomerimpService/SearchCustomerimpByView',
            'oaa_cremake': '厂家资料导入'
        }, {
            'oaa_cid': 'customercimp_cmpc',
            'oaa_cname': '查询子表',
            'oaa_capi': 'CustomerimpService/SearchCustomerimpcByView',
            'oaa_cremake': '厂家资料导入'
        }, ]
    }, {
        'remake': '颜色资料导入',
        'data': [{
            'oaa_cid': 'v_colorset_impInfo',
            'oaa_cname': '查询主表',
            'oaa_capi': 'ColorsetimpService/SearchColorsetimpByView',
            'oaa_cremake': '厂家资料导入'
        }, {
            'oaa_cid': 'colorsetcimp_copc',
            'oaa_cname': '查询子表',
            'oaa_capi': 'ColorsetimpService/SearchColorsetimpcByView',
            'oaa_cremake': '厂家资料导入'
        }, ]
    }, {
        'remake': '期初资料',
        'data': [{
            'oaa_cid': 'stclose_sl',
            'oaa_cname': '查询主表',
            'oaa_capi': 'StockService/SearchStcloseByView',
            'oaa_cremake': '期初资料'
        }, {
            'oaa_cid': 'stclosec_slc',
            'oaa_cname': '查询子表',
            'oaa_capi': 'StockService/SearchStclosecByView',
            'oaa_cremake': '期初资料'
        }, ]
    }, {
        'remake': '期间重算',
        'data': [{
            'oaa_cid': 'stockc_skc',
            'oaa_cname': '期间重算',
            'oaa_capi': 'StockService/RecalculationByWsAndPt',
            'oaa_cremake': '期间重算'
        }, {
            'oaa_cid': 'stclose_sl',
            'oaa_cname': '查询最大期数',
            'oaa_capi': 'StockService/SearchTopStclose',
            'oaa_cremake': '期间重算'
        }, ]
    }, {
        'remake': '送货单',
        'data': [{
            'oaa_cid': 'v_shipInfo',
            'oaa_cname': '送货单主表',
            'oaa_capi': 'ShipService/SearchShipByView',
            'oaa_cremake': '送货单'
        }, {
            'oaa_cid': 'v_shipcInfo',
            'oaa_cname': '送货单子表',
            'oaa_capi': 'ShipService/SearchShipcByView',
            'oaa_cremake': '送货单'
        }, {
            'oaa_cid': 'v_shipMakeInfoAll',
            'oaa_cname': '平衡视图',
            'oaa_capi': 'ShipService/SearchShipAllByView',
            'oaa_cremake': '送货单'
        }, {
            'oaa_cid': 'DTO_shipInfoSum',
            'oaa_cname': '全表汇总',
            'oaa_capi': 'ShipService/GetShipInfoSum',
            'oaa_cremake': '送货单'
        }, {
            'oaa_cid': 'v_shipsalebyView',
            'oaa_cname': '销售单资料',
            'oaa_capi': 'ShipService/SearchShipSaleByView',
            'oaa_cremake': '送货单'
        }, {
            'oaa_cid': 'v_shipcorderbyView',
            'oaa_cname': '订单资料',
            'oaa_capi': 'ShipService/SearchShipCorderByView',
            'oaa_cremake': '送货单'
        }, {
            'oaa_cid': 'v_shipchildbyView',
            'oaa_cname': '销售单商品,订货单商品',
            'oaa_capi': 'ShipService/SearchShipChildByView',
            'oaa_cremake': '送货单'
        }, ]
    },
]


iftemp = "\nif (not exists(select * from objectandapi_oaa where oaa_capi='{}'))"
begintemp = "\nbegin\n{}\nprint '[{}] 完成'\nend"
inserttmep = "insert objectandapi_oaa values('{}','{}','{}','{}')"

sql = '/*\n序号用于快速定位,非正常执行语句\n*/'
index = 1
lst = []
but = "\n\n--重复api"

for item in oaalist:
    sql += '\n\n--{}'.format(item['remake'])
    for n in item['data']:
        oaa_cid = n['oaa_cid']
        oaa_cname = n['oaa_cname']
        oaa_capi = n['oaa_capi']
        oaa_cremake = n['oaa_cremake']
        # if语句
        sqlif = iftemp.format(oaa_capi)
        # insert语句
        sqlin = inserttmep.format(oaa_cid, oaa_cname, oaa_capi, oaa_cremake)
        # begin 语句
        sqlbegin = begintemp.format(sqlin, index)
        sql += sqlif + sqlbegin
        if(oaa_capi in lst):
            but += "\n--[{}] [{}] [{}]".format(index, oaa_capi, oaa_cname)
        else:
            lst.append(oaa_capi)
        index += 1
sql += but
with open(file, 'w') as f:
    f.write(sql)
