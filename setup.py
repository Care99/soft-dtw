from skbuild import setup
DISTNAME = 'soft-dtw'
DESCRIPTION = "Python implementation of soft-DTW"
MAINTAINER = 'Mathieu Blondel,Cesar Rodas'
MAINTAINER_EMAIL = 'cesar_rodas@outlook.com'
LICENSE = 'Simplified BSD'
PACKAGES=['sdtw']
VERSION = '0.1.dev0'
setup(
        configuration=configuration,
        name=DISTNAME,
        version=VERSION,
        description=DESCRIPTION,
        author=MANTAINER,
        license=LICENSE,
        packages=PACKAGES,
        python_requires=">=3.7",
    )
