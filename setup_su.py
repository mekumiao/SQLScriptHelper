#
# 用于系统设置参数sql生成
#  #
from basePath import GetBasePath

file = '{}其他设置2.sql'.format(GetBasePath())

data = [
    {
        "su_cid": "audt_chkdjdate",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "所有库存操作的单据日期不能大于服务器日期",  # 没用
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "corderstock_sh",  # id
        "su_cmodeid": "1",  # 非进销存模块
        "su_ccls": "m",  # 其他参数2模块
        "su_cclsname": "其他参数2",
        "su_cname": "客户订货单订金交纳比例仅考虑已审核的预收款",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "corderstock_chk_post",  # 子元素
    },
    {
        "su_cid": "corderstock_chk_post",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "仅考虑已确认预收款",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "creserveamt",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "预收款是否允许金额为0",  # 需要前端配合!!!
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "corderprod",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "订单和订货变更单审核检查商品停用和库存",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "inputpodesc",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "订单中的非标说明在勾上非标时才能输入",  # 需要前端配合!!!
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "cpoflagbarcode",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "非标商品条码包含订单信息",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "inputpodesc2",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "订单变更单中的非标说明在勾上非标时才能输入 ",  # 需要前端配合!!!
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "movepoflag",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "内部调货单选择库存资料不显示订购说明",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "salecustwareright",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订货单(销售单)保存时,客户资料不受专卖店权限控制",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "saleinputdearea",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "销售模块单据必需输入送货区域",  # 前端配合
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "chdt_chsales",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户交期变更可更改已审核销售单",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "movebyapprove",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "内部调货单启用审批",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "quotsavecustomer",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户意向单保存后更新对应客户资料",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "chclosecorder",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订货变更单自动关闭客户订单",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "creserveaudt_chkpost",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "预收款单确认后不能进行弃审修改",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "polistch_closepolist",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "采购计划变更单自动关闭采购计划",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "vorderch_closevorder",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "采购订单变更单自动关闭采购订单",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "bargainagio",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "特价赠品子折率不允许修改",  # 前端配合
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "djqty_number",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "单据数量只允许整数",  # 待定
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "loan_chkqty",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "借还货单审核检查可用库存量(计算指标)",  # 完成
        "su_ctype": "D",  # D为下拉选项类型
        "su_cdesc": "1",  # 3 已订未出, 2 已销未出, 1 已订未销
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "pocyappcheck",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "订货交期审批",  # 小燕完成
        "su_ctype": "1",
        "su_cdesc": "0",
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "move_chkqty",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "内部调货单检查库存可用量(计算指标)",  # 已有
        "su_ctype": "D",  # D为下拉选项类型
        "su_cdesc": "1",  # 3 已订未出, 2 已销未出, 1 已订未销
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "vin_cdesc2stockc",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "进仓商品说明更新库存备注",  # 备注与相关单据保持一致
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "ddate_ch_corder",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订货单审核时，单据日期改为审核日期",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "ddate_ch_crej",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户退货单审核时，单据日期改为审核日期",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "ddate_ch_move",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "内部调货单审核时，单据日期改为审核日期",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "ddate_ch_transf",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "外部调货单审核时，单据日期改为审核日期",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "pocy_iadvance_land",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订单交货期计算使用商品采购总提前期（陆运）",  # 小燕完成了
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "loan_nofindprice",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "借货单客户借货按弹出资料选择价格",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "vreserve_shou",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "预付款不能大于本单欠款金额",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "corderch_checkvorder",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "已下采购量非标商品对应的客户订货单行次不能变更",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "stkupdate_prodcolor",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "进出仓操作不产生产品颜色子档",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "custmanctl",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户资料受经手人权限管制",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "salesaudt_nodsubamt",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订货单交完款才能审核销售",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "vorder_nochk_polist",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "采购订货量大于采购计划量允许保存",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "rectpricestockc",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "商品调价单审核更新库存资料参考售价和标价",  # 没有这些字段
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "ddate_ch_ship",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "送货单审核时，单据日期改为审核日期",  # 没有送货单
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "stockup_ship",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "备货单审核才能审核送货单",  # 没有送货单
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "move_chkinout",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "内部调货单审核检查调出调入库权限",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "cbatchout",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "出库批号管制",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "autosplit_dj",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "进出库单据明细自动分拆成1数量",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "saleszerocost",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "销售单保存检查成本是否为零",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "corderpost_chk",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订单（变更单）确认后才能审核",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "cordernoclear_mte",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订货单选择商品时不清空相关说明栏位",  # 前端配合
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "ccontractno_stock",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "根据客户合同号进行进出仓",  # 改动大
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "qrystk_nopic",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "库存查询不显示图片",  # 前端配合
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "corder_chchkvorder",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订单变更不检查采购计划及订单",  # 已有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "corder_ddedt_day",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订货单预警天数",  # 完成
        "su_ctype": "T",  # T为输入框
        "su_cdesc": "10",
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "agio_nochk_corder",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订货（销售）单输入时不带入客户折率",  # 前端配合
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "corder_audtchkamt",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订货单审核检查预收金额比例必须大于",  # 已有
        "su_ctype": "T",  # 1为复选框类型
        "su_cdesc": "30",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "updatecustomer",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "不允许相关单据更新客户资料",  # 功能暂时没有
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "rectprice_dcost",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "商品调价单更新产品资料的标准进价",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "1",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "corder_dearea",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订单依送货区域单双号送货",  # 完成
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "dwgridline",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "数据窗口使用格子线",  # 前端配合
        "su_ctype": "1",  # 1为复选框类型
        "su_cdesc": "0",  # 0未选中
        "su_cename": "",
        "su_csubitem": "",
    },
    {
        "su_cid": "deliveryday",
        "su_cmodeid": "1",
        "su_ccls": "m",
        "su_cclsname": "其他参数2",
        "su_cname": "客户订货单默认交货天数：",  # 需要前端配合 [客户订货单的交货日期默认后推 0 天]
        "su_ctype": "T",  #
        "su_cdesc": "0",  #
        "su_cename": "",
        "su_csubitem": "",
    },
]


trantemp = """/*其他参数2*/
BEGIN TRY
BEGIN TRAN
{}
if(@@trancount>0)
commit tran

END TRY
BEGIN CATCH
 select Error_number() as ErrorNumber,  --错误代码
        Error_severity() as ErrorSeverity,  --错误严重级别，级别小于10 try catch 捕获不到
        Error_state() as ErrorState ,  --错误状态码
        Error_Procedure() as ErrorProcedure , --出现错误的存储过程或触发器的名称
        Error_line() as ErrorLine,  --发生错误的行号
        Error_message() as ErrorMessage  --错误的具体信息
   if(@@trancount>0)
      rollback tran
END CATCH
"""

sql = ""

sqltemp = """
IF not exists(select * from setup_su where su_cid='{}')
BEGIN
insert setup_su values('{}','{}','{}','{}','{}','{}','{}','{}','{}')
PRINT '{} 完成 ({})'
END
"""
i = 1

for item in data:
    su_cid = item['su_cid']
    su_cmodeid = item['su_cmodeid']
    su_ccls = item['su_ccls']
    su_cclsname = item['su_cclsname']
    su_cname = item['su_cname']
    su_ctype = item['su_ctype']
    su_cdesc = item['su_cdesc']
    su_cename = item['su_cename']
    su_csubitem = item['su_csubitem']

    sql += sqltemp.format(su_cid, su_cid, su_cmodeid, su_ccls, su_cclsname,
                          su_cname, su_ctype, su_cdesc, su_cename, su_csubitem, i, su_cid)
    i += 1
sql = trantemp.format(sql)
with open(file, 'w') as f:
    f.write(sql)

# txt = ''
# for item in data:
#     su_cname = item['su_cname']
#     txt += "--{}\n".format(su_cname)

# with open('其他设置2-v.txt', 'w') as f:
#     f.write(txt)
