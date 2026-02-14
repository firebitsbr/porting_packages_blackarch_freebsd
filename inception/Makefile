PORTNAME=	inception
DISTVERSION=	455.7c14eb1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A FireWire physical memory manipulation and hacking tool exploiting IEEE 1394 SBP-2 DMA.
WWW=		http://www.breaknenter.org/projects/inception/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/libforensic1394 \
		??/py-libforensic1394@${PY_FLAVOR} \
		??/py-pyusb@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
