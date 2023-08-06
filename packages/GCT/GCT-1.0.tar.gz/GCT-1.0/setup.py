from setuptools import setup, find_packages

setup(
	name='GCT',
	version='1.0',
	packages=find_packages(),
	description='Generate a GCT file',
	long_description=open('README.md').read(),
	url='',
	author='Julien Moehlin',
	license='LICENSE.txt',
	python_requires=">=2.7",
	install_requires=[
		"numpy"
		],
	)