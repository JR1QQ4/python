#!/usr/bin/python
# -*- coding:utf-8 -*-
import census2010

print(census2010.all_data['AK']['Anchorage'])
# {'populations': 291826, 'tracts': 55}

anchoragePop = census2010.all_data['AK']['Anchorage']['populations']
print('The 2010 population of Anchorage was ' + str(anchoragePop))
# The 2010 population of Anchorage was 291826
