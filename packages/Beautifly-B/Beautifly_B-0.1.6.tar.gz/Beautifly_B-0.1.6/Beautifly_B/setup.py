from setuptools import setup

setup(name='Beautifly_B',
      version='0.1.1.1',  # Development release
      description='Beautifly_B team B packages',
      url='https://github.com/azmidri/Beautifly_B',
      author='IE TeamB',
      author_email='azmidri@student.ie.edu',
      license='MIT',
          packages=['Beautifly_B'],
      install_requires=[
          'bokeh,holoviews,matplotlib',
      ],
      zip_safe=False)