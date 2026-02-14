PORTNAME=	roguehostapd
DISTVERSION=	1.0.r45.g381b373
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Hostapd fork including Wi-Fi attacks and providing Python bindings with ctypes.
WWW=		https://github.com/wifiphisher/roguehostapd

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/libnfnetlink \
		??/libnl \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-configparser@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
