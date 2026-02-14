PORTNAME=	gr-gsm
DISTVERSION=	1191.71e9630
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Gnuradio blocks and tools for receiving GSM transmissions.
WWW=		https://github.com/ptrkrysik/gr-gsm

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/graphviz \
		??/log4cpp \
		??/py-yaml@${PY_FLAVOR} \
		??/pybind11 \
		??/swig \
		devel/git

RUN_DEPENDS=	??/boost \
		??/cppunit \
		??/doxygen \
		??/gnuradio \
		??/gnuradio-companion \
		??/gnuradio-osmosdr \
		??/libosmocore \
		??/libosmosdr \
		??/lksctp-tools \
		??/log4cpp \
		??/py-docutils@${PY_FLAVOR} \
		??/py-pyqt5@${PY_FLAVOR} \
		??/py-scipy@${PY_FLAVOR} \
		??/pygtk \
		??/qwt \
		??/swig \
		??/talloc \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
