PORTNAME=	gr-air-modes
DISTVERSION=	396.0b6c383
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Gnuradio tools for receiving Mode S transponder signals, including ADS-B.
WWW=		https://github.com/bistromath/gr-air-modes

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/doxygen \
		devel/git

RUN_DEPENDS=	??/boost \
		??/gnuradio \
		??/gnuradio-companion \
		??/gnuradio-osmosdr \
		??/libuhd \
		??/py-numpy@${PY_FLAVOR} \
		??/py-pyqt4@${PY_FLAVOR} \
		??/py-pyzmq@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/sqlite \
		??/swig


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
