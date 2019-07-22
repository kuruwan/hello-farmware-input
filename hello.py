#!/usr/bin/env python

'''Hello Farmware Input

A simple Farmware example that tells FarmBot to log a new message including the provided input.
'''

from farmware_tools import get_config_value, device

INPUT_VALUE = {{pin63}}/2
device.log(message='Tempurature was: {}'.format(INPUT_VALUE), message_type='success')
