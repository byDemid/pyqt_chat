from setuptools import setup, find_packages

setup(name="mess_client_proj",
      version="0.1",
      description="Client_packet",
      author="Demid Demidov",
      author_email="byDemid.d@yandex.ru",
      packages=find_packages(),
      install_requires=['PyQt5', 'sqlalchemy', 'pycryptodome', 'pycryptodomex']
      )
