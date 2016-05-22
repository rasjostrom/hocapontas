from distutils.core import setup


setup(
    name='hocapontas',
    version='0.1',
    author='Rasmus Sjostrom',
    author_email='ras.sjostrom@hotmail.com',
    packages=[
        'hocapontas', 'hocapontas.scheduler',
        'hocapontas.storage', 'hocapontas.test'
    ],
    url='http://pypi.python.org/pypi/hocapontas/',
    license='GNU GPLv3',
    description='A simple JSON task item scheduler and manager',
    long_description=open('README.rst').read(),
)
