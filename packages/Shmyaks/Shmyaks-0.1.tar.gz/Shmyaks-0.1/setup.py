from setuptools import setup, find_packages

setup(name='Shmyaks',
      version='0.1',
      description='This is package',
      long_description='Really, the funniest around.',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Programming Language :: Python :: 3.9',
      ],
      keywords='package',
      url='http://github.com/Shmyaks',
      author='Shmyaks',
      author_email='maxonic10@list.ru',
      license='MIT',
      packages=find_packages(),
      install_requires=[
      ],
      include_package_data=True,
      zip_safe=False)
