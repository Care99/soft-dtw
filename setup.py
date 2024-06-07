from skbuild import setup
DISTNAME = 'soft-dtw'
DESCRIPTION = "Python implementation of soft-DTW"
MAINTAINER = 'Mathieu Blondel,Cesar Rodas'
MAINTAINER_EMAIL = 'cesar_rodas@outlook.com'
LICENSE = 'Simplified BSD'
PACKAGES=['sdtw']
VERSION = '0.1.dev0'
CMAKE_INSTALL_DIR='sdtw'
setup(
        name=DISTNAME,
        version=VERSION,
        description=DESCRIPTION,
        author=MAINTAINER,
        license=LICENSE,
        packages=PACKAGES,
        python_requires=">=3.7",
        cmake_install_dir=CMAKE_INSTALL_DIR,
    )
