from setuptools import setup, find_packages

setup(name="py_alex_mess_server",
      version="0.1.1",
      description="Alex Mess Server",
      author="Alex",
      author_email="momot-717@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex'],
      scripts=['server/server_run']
      )
