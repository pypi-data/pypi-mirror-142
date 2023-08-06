from setuptools import find_packages, setup

setup(
    name='flat-me',
    packages=find_packages(),
    version='0.1.5',
    description='File conversion/transformation tool',
    author='uncomfortablepanda',
    license='Apache 2.0',
    install_requires=['PyInquirer','pyfiglet','pandas','pathlib'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    test_suite='tests',
    entry_points= {'console_scripts': ['flat-me=flat_me.user_prompt:main']}
)