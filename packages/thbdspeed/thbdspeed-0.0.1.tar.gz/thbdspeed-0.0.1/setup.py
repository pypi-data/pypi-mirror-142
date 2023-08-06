from setuptools import setup, find_packages
#MAO2116
setup(
    name='thbdspeed',
    packages=find_packages(),
    include_package_data=True,
    version="0.0.1",
    description='SIMPLE INTERNET SPEED TESTING TOOL.',
    author='Moajjem',
    author_email='smmoajjem@gmail.com',
    long_description=(open("README.md","r")).read(),
    long_description_content_type="text/markdown",
   install_requires=['lolcat'],
 
    keywords=['hacker', 'spam', 'tool', 'sms', 'bomber', 'call', 'prank', 'termux', 'hack','sms bomber','sms bomber', 'AKXVAU','TOXIC-VIRUS','TOXIC-SOUL','INTERNET SPEED','SPEED TEST','INTERNET'],
    classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'Topic :: Software Development :: Libraries :: Python Modules',
            'License :: OSI Approved :: MIT License',
            'Programming Language :: Python :: 3',
            'Operating System :: OS Independent',
            'Environment :: Console',
    ],
    
    license='MIT',
    entry_points={
            'console_scripts': [
                'thbdspeed = thbdspeed.thbdspeed:menu',
                
            ],
    },
    python_requires='>=3.9'
)
