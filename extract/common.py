import yaml

__config = None

def config():
	global __config
	if not __config:
		with open('config.yaml') as f:
			__config = yaml.load(f)

	return __config