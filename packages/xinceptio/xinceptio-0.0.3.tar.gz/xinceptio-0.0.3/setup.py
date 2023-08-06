'''
Author: Xin Zong
Date: 2022-03-11 16:54:15
LastEditors: Xin Zong
LastEditTime: 2022-03-11 19:32:33
FilePath: /pip_package/setup.py
'''
#!/usr/bin/env python
from setuptools import find_packages, setup
requirements = [
    'matplotlib'
]
__version__ = "V0.0.3"

if __name__ == '__main__':

    # print(find_packages())
    # setup(
    #     name='xinceptio',
    #     version=__version__,
    #     description='dms-fatigue-oracle',
    #     author='Zong Xin',
    #     author_email='xin.zong@inceptio.ai',
    #     # packages=find_packages(),
    #     classifiers=[
    #         'Development Status :: 4 - Beta',
    #         'License :: OSI Approved :: Apache Software License',
    #         'Operating System :: OS Independent',
    #         'Programming Language :: Python :: 3',
    #     ],
    #     # classifiers=[
    #     #     "Programming Language :: Python :: 3",
    #     #     "Operating System :: OS Independent",
    #     # ],
    #     package_dir={"": "xinceptio"},
    #     packages=find_packages(where="xinceptio"),
    #     python_requires=">=3.6",

    #     zip_safe=False)

    setup(
        name='xinceptio',
        version=__version__,
        description='DSM Oracle',
        author='Zong Xin',
        author_email='xin.zong@inceptio.ai',
        python_requires=">=3.6",
        requirements=requirements,
        packages=['xinceptio'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: Apache Software License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Utilities',
            'Topic :: Software Development',
            'Topic :: Security',
        ],
        license='Apache License 2.0',)


 
# setup(name="xinceptio", version="1.0", description="oracle of dms fatigue-score inference", author="zong xin", package_dir = {'xinceptio': 'lib'})


