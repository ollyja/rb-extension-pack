#!/usr/bin/env python

from reviewboard.extensions.packaging import setup

from rbdesignfield import get_package_version


PACKAGE = 'rbdesignfield'

setup(
    name=PACKAGE,
    version=get_package_version(),
    description='Adds a designboard field to point to the design.',
    url='http://www.pipahr.com/',
    author='Pipapai Inc.',
    author_email='support@pipapai.com',
    maintainer='Pipapai Inc.',
    maintainer_email='support@pipapai.com',
    packages=['rbdesignfield'],
    entry_points={
        'reviewboard.extensions': [
            'rbdesignfield = rbdesignfield.extension:DesignFieldExtension',
        ],
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Review Board',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
