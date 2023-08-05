from setuptools import setup, find_packages

setup(
    name='grappelli-modeltranslation2',
    version='0.1.4',
    description="A small compatibility layer between grappelli and django-modeltranslation",
    author='Jacob Magnusson',
    author_email='m@jacobian.se',
    url='https://github.com/jmagnusson/grappelli-modeltranslation',
    license='New BSD License',
    packages=find_packages(),
    platforms=['any'],
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=['django', 'django-grappelli'],
    package_data={'grappelli_extensions': [
        'static/grappelli_modeltranslation/css/*.css',
        'static/grappelli_modeltranslation/js/*.css',
    ]},
)
