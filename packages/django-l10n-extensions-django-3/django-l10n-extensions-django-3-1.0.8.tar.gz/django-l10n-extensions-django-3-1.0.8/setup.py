from setuptools import find_packages, setup

setup(
    name='django-l10n-extensions-django-3',
    version='1.0.8',
    author=u'Jon Miller',
    author_email='iamjonamiller@gmail.com',
    package_dir={'': 'src'},
    packages=find_packages(where='./src'),
    include_package_data=True,
    install_requires=['Django>=3.2.12', 'polib>=1.0'],
    url='https://github.com/iamjonmiller/django-l10n-extensions',
    license='',
    description=open('DESCRIPTION').read(),
    long_description=open('README.md').read(),
    zip_safe=False,
    key_words=['django', 'l10n', ]
)
