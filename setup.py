from setuptools import setup, find_packages

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    # This is the name of your project. The first time you publish this
   
    name='DateandTime',  # Required
    version='1.0.0',  # Required

    # This is a one-line description or tagline of what your project does. This
    # corresponds to the "Summary" metadata field:
    # https://packaging.python.org/specifications/core-metadata/#summary
    description=' It Tells you the date and time',  # Optional

    
    # long_description=long_description,  # Optional

    long_description_content_type='text/markdown',    
    url='https://github.com/odhiambocuttice/myfirstproject',  # Optional

    author='Odhiambo Cuttice',  # Optional

    # This should be a valid email address corresponding to the author listed
    # above.
    author_email='odhiambocuttice@gmail.com',  # Optional

    # Classifiers help users find your project by categorizing it.
        classifiers=[  # Optional
      
        'Development Status :: 2- Alpha',# maturity of my project
        'Intended Audience :: python users',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        ],
    keywords='date and time program',  # Optional
    packages=find_packages('mycode.py'),  # Required

    # Specify which Python versions you support. In contrast to the
      python_requires='>=3.6',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
     install_requires=['DateTime'],  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
   #   extras_require={  # Optional
      #  'dev': ['check-manifest'],
      #  'test': ['coverage'],
   # },

    # If there are data files included in your packages that need to be
    #   package_data={  # Optional
    #    'sample': ['package_data.dat'],
    #},

    

   