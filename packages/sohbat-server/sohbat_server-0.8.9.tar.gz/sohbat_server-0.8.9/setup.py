from setuptools import setup, find_packages

setup(name='sohbat_server',
      version='0.8.9',
      description='sohbat_server',
      author='Joksar',
      author_email='politer72@gmail.com',
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )