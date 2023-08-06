from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='nreip_api',
    version='1.0.0',
    author = 'Wasyan',
    author_email='vasyan93@gmail.com',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.txt')).read(),
    url='https://github.com/Native-Robotics/EthernetIP',
    download_url='https://github.com/Native-Robotics/EthernetIPethernetip/linux/nreip_api.zip',  
)



