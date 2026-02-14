PORTNAME=	libxtrx
DISTVERSION=	78.d9599fb
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	High level API for the xtrx SDR.
WWW=		https://github.com/xtrx-sdr/libxtrx

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		devel/git

RUN_DEPENDS=	??/liblms7002m-xtrx \
		??/libxtrxdsp \
		??/libxtrxll \
		??/qcustomplot \
		??/soapysdr


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
