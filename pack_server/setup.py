from setuptools import setup, find_packages

setup(name="mess_server_proj",
      version="0.1",
      description="Server packet",
      packages=find_packages(),
      author="Demid Demidov",
      author_email="byDemid.d@yandex.ru",
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
