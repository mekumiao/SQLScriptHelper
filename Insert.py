import json

jsonpath = r"C:\Users\Administrator\Desktop\stclosec_slc.json"

with open(jsonpath, 'r', encoding='utf8') as f:
    jsonstr = f.read()

data = json.loads(jsonstr)

inserttemp = "INSERT stclosec_slc VALUES({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})"
sql = r'\*期间子表数据*\\n\n'

for item in data:
    slc_cfeatureid1 = item['slc_cfeatureid1']
    slc_cfeatureid3 = item['slc_cfeatureid3']
    slc_cfeatureallid = item['slc_cfeatureallid']
    slc_cbatch = item['slc_cbatch']
    slc_minitqty = item['slc_minitqty']
    slc_mprice = item['slc_mprice']
    slc_dlastindt = item['slc_dlastindt']
    slc_cremark2 = item['slc_cremark2']
    slc_dvalidity = item['slc_dvalidity']
    slc_ijoborder = item['slc_ijoborder']
    sl_iitem = item['sl_iitem']
    slc_cfeatureid2 = item['slc_cfeatureid2']
    ws_cwhid = item['ws_cwhid']
    slc_item = item['slc_item']
    pt_cmteid = item['pt_cmteid']
    slc_mendqty = item['slc_mendqty']
    slc_cremark = item['slc_cremark']
    slc_cjobcode = item['slc_cjobcode']
    sql += inserttemp.format(slc_cfeatureid1, slc_cfeatureid3, slc_cfeatureallid, slc_cbatch, slc_minitqty, slc_mprice, slc_dlastindt, slc_cremark2,slc_dvalidity, slc_ijoborder, sl_iitem, slc_cfeatureid2, ws_cwhid, slc_item, pt_cmteid, slc_mendqty, slc_cremark, slc_cjobcode)
    sql += '\n'

print(sql)
