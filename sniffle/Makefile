PORTNAME=	sniffle
DISTVERSION=	v1.11.0.r0.g18252f2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A sniffer for Bluetooth 5 and 4.x LE.
WWW=		https://github.com/nccgroup/Sniffle

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/arm-none-eabi-gcc \
		??/cmake \
		devel/git

RUN_DEPENDS=	??/py-pyserial@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
