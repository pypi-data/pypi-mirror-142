import os, sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    try:
        import wheel

        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist upload')
    os.system('python setup.py bdist_wheel upload')
    sys.exit()

setup(
    name='django-customize-history1',
    version='1.0.1',
    license='MIT',
    author="Mayur Ariwala",
    author_email='mayur@softices.com',
    packages=['django_customize_history'],
    include_package_data=True,
    url='https://github.com/mayur-softices/djnago-customize-history/',
    keywords='Django Customize History',
    install_requires=[
        'django',
    ],
    zip_safe=False,
)
