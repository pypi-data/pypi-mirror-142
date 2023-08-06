#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2022/3/9 14:23
@Author   : ji hao ran
@File     : test.py
@Project  : pkgDev
@Software : PyCharm
"""

from jhrtools import *

if __name__ == '__main__':
    # ab = Rtdb(point=['LGHB.WGQF8.G1N1S3201HL01NB.P', 'LGHB.WGQF8.G1N1S3201HL02NB.P',
    #                  'LGHB.WGQF8.G1N1S3201HL03NB.P'
    #                  ], start_time='2021-1-1', end_time='2021-5-1').query_history()
    #
    # print(Mysql().read(table_names='tb_tenant'))
    #
    # r = RuleMatch(tenant_id='SHZRBWG',
    #               project_id='SHZRBWG',
    #               rb=Rule().rb,
    #               pt=RTDBPointTable().pt)
    # print(r.available_rules)

    df = RTDBPointTable().pt
    print(df.head())

    Kafka().produce(1)
