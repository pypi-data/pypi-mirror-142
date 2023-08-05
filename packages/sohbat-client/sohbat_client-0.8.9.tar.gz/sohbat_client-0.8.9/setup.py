from setuptools import setup, find_packages

setup(name='sohbat_client',
      version='0.8.9',
      description='sohbat_client',
      author='Joksar',
      author_email='politer72@gmail.com',
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )