# -*- coding: utf-8 -*-
"""
Created on 2017/12/21.

@author: kesong
"""
import sys

import executors
from constant import *


def exec_params(params):
	try:
		params_dict = dict()
		params_dict['script'] = "handler/" + params[1] + ".py"

		params_dict['cmptype'] = params[2]

		params_dict['tabletype'] = params[3]
		if params[2] == CmpType.SINGLE_DATABASE:
			params_dict['database'] = params[4]
		elif params[2] == CmpType.SINGLE_TABLE:
			params_dict['table'] = params[4]

		sample = False
		if Strategy.USE_SAMPLE in params:
			sample = True
		params_dict['sample'] = sample

		if sample:
			params_dict['divisor'] = params[-2]
			params_dict['mod'] = params[-1]
	except IndexError as e:
		print e
		print "paramter list:"
		print "script name: example:peta_hive_count"
		print "cmptype:single_database==>database name / single_table==> table name / all_database / all_table"
		print "tabletype: valid invalid invaliddetail pre"
		print "optional parameters: sample==>divisor==>mod"
		sys.exit(0)

	return params_dict


if __name__ == "__main__":
    param_dict = exec_params(sys.argv)
    print param_dict

    if param_dict['cmptype'] == CmpType.SINGLE_TABLE:
        executors.single_table(param_dict)
    elif param_dict['cmptype'] == CmpType.ALL_TABLE:
        executors.all_table(param_dict)
    elif param_dict['cmptype'] == CmpType.SINGLE_DATABASE:
        executors.single_database(param_dict)
    else:
        executors.all_database(param_dict)
