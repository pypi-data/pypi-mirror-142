from setuptools import setup

setup(
    name='cryptoEx',
    version='0.0.3',
    author='Tiancheng Jiao',
    author_email='jtc1246@outlook.com',
    url='https://github.com/jtc1246/cryptoEx',
    description='A simple API for some cryptocurrency exchanges',
    packages=['cryptoEx'],
    install_requires=['urllib3'],
    python_requires='>=3',
    platforms=["all"],
    license='GPL-2.0 License'
)