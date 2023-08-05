#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time     : 2022/3/9 13:09
@Author   : ji hao ran
@File     : rtdb.py
@Project  : pkgDev
@Software : PyCharm
"""

import pandas as pd
from typing import List, Union
from .data_source import Mysql
from functools import reduce

"""
rtdb-v10 标准实时库相关操作
"""


class RTDBPointTable:
    """
    RTDB_V10 点位表
    """

    def __init__(self,
                 rtdb_host: str = '192.168.1.240',
                 rtdb_name: str = 'jet_rtdb_v10_prod_4_hongbo',
                 project_host: str = '192.168.1.244',
                 project_name: Union[List[str], str] = 'jet_101_shzg_dev'):
        """

        :param rtdb_host: 实时库的数据库主机
        :param rtdb_name: 实时库的数据库名字
        :param project_host: 项目的数据库主机
        :param project_name: 项目的数据库名字
        """
        self.rtdb_host = rtdb_host
        self.rtdb_name = rtdb_name
        self.project_host = project_host
        self.project_name = project_name if isinstance(project_name, list) else [project_name]

    @property
    def _rtdb(self):
        """实时库相关表"""
        # 实时库连接
        rtdb_con = Mysql(host=self.rtdb_host, name=self.rtdb_name)
        # 实时库系列表
        tb_tenant, tb_project, tb_meter, tb_point = rtdb_con.read(["tb_tenant", "tb_project", "tb_meter", "tb_point"])
        # 实时库表选择列
        tenant = tb_tenant[['tenant_id', 'tenant_name']]
        project = tb_project[['tenant_id', 'project_id', 'project_name']]
        meter = tb_meter[['tenant_id', 'project_id', 'meter_id', 'meter_name']]
        point = tb_point[['tenant_id', 'project_id', 'meter_id', 'point_id', 'point_name']]
        return tenant, project, meter, point

    @staticmethod
    def _single_project(con):
        """单个项目表"""
        # 项目系列表
        tb_equip, tb_sys_type, tb_equip_type = con.read(["tb_equip", "tb_sys_equip_sys_type", "tb_sys_equip_type"])
        # 项目表选择列
        equip = tb_equip[
            ['equip_sys_type_id', 'equip_sys_id', 'equip_type', 'equip_id', 'template_id', 'equip_name',
             'rtdb_meter_id']
        ].rename(columns={'rtdb_meter_id': 'meter_id'})
        sys_type = tb_sys_type[['equip_sys_type_id', 'equip_sys_type_name']]
        equip_type = tb_equip_type[['equip_type_id', 'equip_type_name']].rename(columns={'equip_type_id': 'equip_type'})
        return equip, sys_type, equip_type

    @property
    def _project(self):
        """合并所有项目表"""
        # 所有项目
        project_tables = [self._single_project(Mysql(host=self.project_host, name=i)) for i in self.project_name]
        # 设备表
        equip = pd.concat([i[0] for i in project_tables])
        # 系统类型表
        sys_type = pd.concat([i[1] for i in project_tables])
        # 设备类型表
        equip_type = pd.concat([i[2] for i in project_tables])
        return equip, sys_type, equip_type

    @property
    def pt(self):
        """点位表"""
        # 实时库表
        tenant, project, meter, point = self._rtdb
        # 合并
        m_df = reduce(lambda x, y: pd.merge(x, y, how='left'), [point, *self._rtdb, *self._project])
        # 增加点位id和点位名列
        m_df['rtdb_id'] = m_df[['tenant_id', 'project_id', 'meter_id', 'point_id']].apply(
            lambda x: '.'.join([f'{i}' for i in x]), axis=1)
        m_df['rtdb_name'] = m_df[['tenant_name', 'project_name', 'meter_name', 'point_name']].apply(
            lambda x: '.'.join([f'{i}' for i in x]), axis=1)
        # return
        return m_df
