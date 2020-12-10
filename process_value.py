import os
import json
from collections import OrderedDict
import sys

folder_path =  sys.argv[1]

for folder in os.listdir(folder_path):
	for subfolder in os.listdir(os.path.join(folder_path, folder)):
		print(os.path.join(folder_path, folder, subfolder, "metrics.jsonl"))
		if os.path.isfile(os.path.join(folder_path, folder, subfolder, "metrics.jsonl")):
			metricList = []
			with open(os.path.join(folder_path, folder, subfolder, "metrics.jsonl")) as f:
				for jsonObj in f:
					metricDict = json.loads(jsonObj, object_pairs_hook = OrderedDict)
					if 'value' in metricDict:
						if isinstance(metricDict['value'], str):
							metricDict['valueStr'] = metricDict['value']
							del metricDict['value']
						elif isinstance(metricDict['value'], int):
							metricDict['valueInt'] = metricDict['value']
							del metricDict['value']
						elif isinstance(metricDict['value'], float):
							metricDict['valueFloat'] = metricDict['value']
							del metricDict['value']
						elif isinstance(metricDict['value'], OrderedDict):
							metricDict['valueDict'] = metricDict['value']
							del metricDict['value']
						else:
							print(type(metricDict['value']), end='')
					metricList.append(metricDict)
			outstr = ""
			for line in metricList:
				outstr += json.dumps(line) + '\n'
			with open(os.path.join(folder_path, folder, subfolder, "metrics.jsonl"), 'w') as outfile:
				outfile.write(outstr)