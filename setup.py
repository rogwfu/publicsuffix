from distutils.core import setup


setup(
    name='publicsuffix',
    version='0.1',
    description='Python interface to the Public Suffix List',
    author='Joel Watts',
    author_email='joel@joelwatts.com',
    url='http://github.com/jpwatts/publicsuffix',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    packages=['publicsuffix'],
	package_dir={'publicsuffix': 'publicsuffix'},
	package_data={'publicsuffix': ['public_suffix_list.txt']},

	install_requires=[
	  "httplib2 >= 2-0.8"
	  ],
)
