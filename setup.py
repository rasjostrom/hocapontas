from distutils.core import setup


setup(
    name='hocapontas',
    version='0.0.1',
    author='Rasmus Sjostrom',
    author_email='ras.sjostrom@hotmail.com',
    packages=[
        'hocapontas', 'hocapontas.scheduler',
        'hocapontas.storage'
    ],
    url='http://pypi.python.org/pypi/hocapontas/',
    license='GNU GPLv3',
    description='A simple life-assistant API',
    long_description=open('README.rst').read(),
)
