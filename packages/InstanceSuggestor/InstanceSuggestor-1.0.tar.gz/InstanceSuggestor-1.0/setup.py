#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages

setup(
	author = 'Shruti Sharma',
	author_email = "shruti.sharma@netbook.ai",
	classifiers = [
	'Programming Language :: Python :: 3.9'],
	description = "An cloud instance suggestor",
	include_package_data = True,
	name = 'InstanceSuggestor',
	version = '1.0',
	zip_safe = False,
	packages = find_packages()
	)

