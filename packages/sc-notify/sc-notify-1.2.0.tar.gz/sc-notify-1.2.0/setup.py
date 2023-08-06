
from setuptools import setup, find_packages

# This call to setup() does all the work
setup(
  name="sc-notify",
  version="1.2.0",
  description="Slack and Email notifier for automated builds and more",
  author="SimonComputing, Inc.",
  author_email="simon@simoncomputing.com",
  packages=find_packages(exclude=('test', 'venv', 'doc_build', 'doc_source', 'build', 'dist')),
  install_requires=['slackclient==2.5.0'],
  include_package_data=True,
  entry_points={
    "console_scripts": [
      'notify=notify.__main__:main'
    ]
  }
)
