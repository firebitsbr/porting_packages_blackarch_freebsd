PORTNAME=	rvi-capture
DISTVERSION=	14.a2e129b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Capture packets sent or received by iOS devices.
WWW=		https://github.com/gh2o/rvi_capture

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/libimobiledevice \
		??/usbmuxd \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
