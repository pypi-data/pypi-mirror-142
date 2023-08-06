__author__ = 'Julien Moehlin'

import numpy as np

class GCT(object):
	"""
	"""
	def __init__(self, df):
		self.data = df
		self.rows = df.shape[0]
		self.columns = df.shape[1]
		self.name = df['Name']
		self.description = 0
		if 'Description' in self.data.columns :
			self.columns = self.columns - 2
		else:
			self.columns = self.columns - 1
			self.data.insert(1, 'Description', np.nan)

	def generate(self, output):
		with open(output, 'w') as output_file:
			output_file.write('#1.2\n')
			output_file.write(f'{self.rows}\t{self.columns}\n')
			for i in self.data.columns.tolist():
				output_file.write(f'{i}\t')
			output_file.write('\n')
			df = self.data.to_string(header=False, index=False, index_names=False).split('\n')
			df = ['\t'.join(x.split()) + '\n' for x in df]
			for i in df:
				output_file.write(f'{i}')

"""
class CLS(object):
	def __init__(self, total, number_classe):
		self.total = total
		self.number_classe = number_classe

	def generate(self, cls_object):
		pass
"""