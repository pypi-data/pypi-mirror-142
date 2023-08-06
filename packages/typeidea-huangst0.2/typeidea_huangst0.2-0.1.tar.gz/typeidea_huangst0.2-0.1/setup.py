from setuptools import setup, find_packages

setup(
    name = 'typeidea_huangst0.2',
    version = '0.1',
    description= 'Blog System base on Django',
    author='huangst',
    author_email='huangst21@lzu.edu.cn',
    url = 'https://www.huangst21.com',
    license='MIT',
    packages= find_packages('typeidea'),
    package_dir={'': 'typeidea'},
    package_data = {'': [
        'themes/*/*/*/*',
    ]},
    extras_require = {
        'ipython': ["ipython==6.2.1"]
    },
    scripts=[
        'typeidea/manage.py'
        ,
    ],
    entry_points = {
        'console_scripts': [
            'typeidea_manage = manage:main',

        ]
    },

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development :: Libraries',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.8',
    ],

)
