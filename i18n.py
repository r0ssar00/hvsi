# coding=utf-8
import copy, fnmatch, os
import pkg_resources
i18n_global = {}
try:
	files = pkg_resources.resource_listdir(__name__,'')
except:
	files = os.listdir('.')
for file in fnmatch.filter(files, "i18n_*.py"):
	if 'diff' in file:
		continue
	code = file.replace('i18n_','').replace('.py','').replace('_','-')
	mod = file.replace('.py','')
	try:
		i18n_global[code] = __import__('hvsi.' + mod, fromlist=[mod]).i18n
	except:
		i18n_global[code] = __import__(mod, fromlist=[mod]).i18n
def update_dict(orig, new):
	for k in new:
		if isinstance(new[k], dict):
			if k not in orig:
				orig[k] = new[k]
			else:
				update_dict(orig[k], new[k])
		else:
			orig[k] = new[k]
class i18n_over():
	def __init__(self, over=None):
		self.o = True if over else False
		if over:
			self.i18n = copy.deepcopy(i18n_global)
			update_dict(self.i18n, over)
	def __getitem__(self, i):
		if self.o:
			return self.i18n[i]
		else:
			return i18n_global[i]
	def __iter__(self):
		if self.o:
			return self.i18n.__iter__()
		else:
			return i18n_global.__iter__()
	def keys(self):
		if self.o:
			return self.i18n.keys()
		else:
			return i18n_global.keys()
def override_title(page, en, fr):
	return i18n_over(
		{
			'e': {
				'pages': {
					page: {
						'title': en
					}
				}
			},
			'f': {
				'pages': {
					page: {
						'title': fr
					}
				}
			}
		})
i18n = i18n_over()
