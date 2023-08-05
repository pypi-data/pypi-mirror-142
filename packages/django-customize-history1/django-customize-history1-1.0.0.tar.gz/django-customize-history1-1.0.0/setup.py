from setuptools import setup, find_packages

setup(
    name='django-customize-history1',
    version='1.0.0',
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

)
