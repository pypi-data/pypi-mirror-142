from setuptools import setup, find_packages

setup(name="py_alex_mess_client",
      version="0.1.0",
      description="Alex Mess Client",
      author="Alex",
      author_email="momot-717@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
