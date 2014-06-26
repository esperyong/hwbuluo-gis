from __future__ import absolute_import
from setuptools import setup, find_packages
import sys
import hwbuluo.contrib.gis as gis

readme_file = 'README.mkd'
try:
    long_description = open(readme_file).read()
except IOError:
    sys.stderr.write("[ERROR] Cannot find file specified as "
        "``long_description`` (%s)\n" % readme_file)
    sys.exit(1)

setup(name='hwbuluo-gis',
      version=gis.get_version(),
      description='hwbuluo site gis dev package',
      long_description=long_description,
      zip_safe=False,
      author='Liuyong',
      author_email='esperyong@gmail.com',
      url='https://esperyong@bitbucket.org/esperyong/hwbuluo-gis.git',
      download_url='https://bitbucket.org/esperyong/hwbuluo-gis/get',
      packages = find_packages(exclude=['demo', 'demo.*']),
      include_package_data=True,
      install_requires = [
        'git+https://github.com/tkrajina/gpxpy.git',
        'lxml>=3.3.5',
        ### Required to build documentation
        # 'sphinx',
        # 'south',
      ],
      #test_suite='tests.main',
      classifiers = ['Development Status :: 4 - Beta',
                     'Environment :: Web Environment',
                     #'Framework :: Django',
                     'Intended Audience :: Developers',
                     'License :: OSI Approved :: BSD License',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python',
                     'Topic :: Utilities'],
      )


