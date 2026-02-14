PORTNAME=	sparrow-wifi
DISTVERSION=	219.38b0312
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Next-Gen GUI-based WiFi and Bluetooth Analyzer.
WWW=		https://github.com/ghostop14/sparrow-wifi

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/gpsd \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
