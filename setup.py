from setuptools import setup

setup(
    name='mibplugin',
    version='0.0.1',
    author='saghosh',
    author_email = 'saghosh@infinera.com',
    description='Mib Compilation and Loading',
    packages=['mibplugin.compile', 'mibplugin.loader', 'mibplugin.temporaryContainer']
)