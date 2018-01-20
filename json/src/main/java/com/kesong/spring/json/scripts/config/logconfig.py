# -*- coding: utf-8 -*-
# 日志模板
"""
Created on 2017/12/5.

@author: kesong
"""
count_peta_hive_title = "count----------- petadata & hive------------"
count_pgp_hive_title = "count-------------pgp & hive-----------------"
count_emr_hive_title = "count-------------emr & hive-----------------"
count_ods_hive_title = "count-------------ods & hive-----------------"
count_head = "%s需要统计的表数量为: %s"
count_schema = "对比的表名\thive数据量\tpetadata数据量"
counterror_schema = "数量不同的表\thive数据量\tpetadata数据量"
count_pgphive_schema = "对比的表名\thive数据量\tpgp数据量"
counterror_pgphive_schema = "数量不同的表\thive数据量\tpgp数据量"
count_emrhive_schema = "对比的表名\thive数据量\temr数据量"
counterror_emrhive_schema = "数量不同的表\thive数据量\temr数据量"
count_odshive_schema = "对比的表名\thive数据量\tods数据量"
counterror_odshive_schema = "数量不同的表\thive数据量\tods数据量"
count_tail = "相同数量：%d\t不同数量：%d\t总耗时：%ds"

field_peta_hive_title = "field-------------petadata & hive------------------"
field_head = "比较部门：%s 表数量：%s"
field_schema = "字段\thive数据\tpetadata数据\t对比结果"
fielderror_schema = "字段\thive数据\tpetadata数据\t对比结果"
field_result = "相同字段数：%s\t不同字段数：%s\t"
field_tail = "当前表对比完毕！\t耗时：%.2fs\t异常行数：%s\t"