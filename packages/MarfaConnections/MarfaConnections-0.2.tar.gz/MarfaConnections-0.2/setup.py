from setuptools import setup, find_packages

setup(name='MarfaConnections',
      version='0.2',
      description='for connection',
      long_description='Really, the funniest around.',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3',
          'Topic :: Text Processing :: Linguistic',
      ],
      keywords='marfatech connections lib',
      author='Ruslan Galimov',
      author_email='rgalimov@marfa-tech.com',
      license='MIT',
      packages=find_packages(),
      install_requires=[
          'SQLAlchemy',
          'sqlalchemy-migrate',
          'sshtunnel',
          'PyYAML',
          'pymysql',
          'pandas'
      ],
      include_package_data=True,
      zip_safe=False)