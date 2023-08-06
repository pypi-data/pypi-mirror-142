from setuptools import setup, find_packages
__version__ = '3.2.0'
setup(
        name='rewal',
        version=__version__,
        packages=find_packages(),
        url='https://www.github.com/iamtalhaasghar/rewal',
        author='Talha Asghar',
        author_email='talhaasghar.contact@simplelogin.fr',
        description='A utility that downloads wallpapers from reddit',
        install_requires=[i for i in open('requirements.txt').readlines() if len(i)!=0],
        package_data={
            'wpreddit': ['fonts/*.otf', 'conf_files/*.conf', 'conf_files/*.desktop']
        },
        entry_points={
            'console_scripts': [
                'rewal = wpreddit.main:run'
            ]
        }
)
