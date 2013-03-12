#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Staffa
#
# Created:     12.03.2013
# Copyright:   (c) Staffa 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------

chart.extend([0]*256)
# Побайтовое чтение файла
s = input('Укажите полный адрес файла для обработки')
with open(s,r) as f:
    byte = f.read(1)
    while byte:
        counter = chart.pop(ord(byte))
        chart.insert(ord(byte),counter)
        byte = f.read(1)

import array
def list2str(list):
    return array.array('B',list).tostring()
