from io import open
from setuptools import setup

version = '1.0.2'

setup(
    name='mikhailok_convertor', version=version,

    author='MikhailOk',
    author_email='mikhail.okhapkin@yandex.ru',

    url='https://github.com/MikhailOk-creator/Convertor',
    download_url='https://github.com/MikhailOk-creator/Convertor/archive/refs/heads/master.zip'.format(
        version
    ),

    packages=['mikhailok_convertor']
)