from setuptools import setup

setup(
    name='zservices',
    packages=['dynamodb', 'mongodb', 's3'],
    package_dir={'dynamodb': 'dynamodb', 'mongodb': 'mongodb', 's3': 's3'},
    version='0.0.5',
    license='MIT',
    platforms='cross-platfom, platform-independent',
    description='ZFunds basic services',
    long_description='Dependencies: coming soon',
    author='Yogesh Yadav',
    author_email='yogesh@zfunds.in',
    keywords=['dynamodb', 'mongodb', 's3'],
    install_requires=[
        'python-dotenv==0.19.2', 'boto3==1.21.17'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 3.10',
    ],
)
