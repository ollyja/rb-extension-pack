#!/usr/bin/env python

from reviewboard.extensions.packaging import setup

from rbdraftcheck import get_package_version


PACKAGE = 'rbdraftcheck'

setup(
    name=PACKAGE,
    version=get_package_version(),
    description='Check Draft Content before publishing',
    url='https://www.reviewboard.org/',
    author='Pipapai Inc.',
    author_email='chunlei@pipapai.com',
    maintainer='Pipapai Inc.',
    maintainer_email='support@pipapai.com',
    packages=['rbdraftcheck'],
    entry_points={
        'reviewboard.extensions':
            '%s = %s.extension:DraftCheckExtension' % (PACKAGE, PACKAGE)
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
