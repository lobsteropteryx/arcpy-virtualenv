from setuptools import setup

setup(
  name='esri_virtualenv',
  version='windows_10.5',
  description='A .pth file to consume arcpy from a virtualenv',
  package_data={'esri_virtualenv': 'windows_10.5.pth'},
  include_package_data=True,
  install_requires=[]
)
