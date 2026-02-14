PORTNAME=	gr-paint
DISTVERSION=	53.c443e36
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An OFDM Spectrum Painter for GNU Radio.
WWW=		https://github.com/drmpeg/gr-paint

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/boost \
		??/cmake \
		??/doxygen \
		??/pybind11 \
		devel/git

RUN_DEPENDS=	??/gnuradio \
		??/gnuradio-companion \
		??/py-pillow@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
