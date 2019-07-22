#!/usr/bin/env python

'''Hello Farmware Input

A simple Farmware example that tells FarmBot to log a new message including the provided input.
'''

from farmware_tools import get_config_value, device

INPUT_VALUE = get_pin_value(63)
device.log(message='Hello Farmware! Input was: {}'.format(INPUT_VALUE), message_type='success')
