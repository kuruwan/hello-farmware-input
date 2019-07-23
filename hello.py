#!/usr/bin/env python

'''Hello Farmware Input

A simple Farmware example that tells FarmBot to log a new message including the provided input.
temp = {{pin63}}
    {"name": "input", "label": "Input (temputature)", "value": "default"}
    {"name": "temp", "label": "Input (tempin)", "value": "default"}
'''

from farmware_tools import get_config_value, device

INPUT_VALUE = get_config_value(farmware_name='Hello Farmware Input', config_name='input', value_type=str)
INPUT_VALUE2 = get_config_value(farmware_name='Hello Farmware Input2', config_name='temp', value_type=str)
device.log(message='Hello Farmware! Input was: {}'.format(INPUT_VALUE), message_type='success')
