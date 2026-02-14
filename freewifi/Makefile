PORTNAME=	freewifi
DISTVERSION=	30.1cb752b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	How to get free wifi.
WWW=		https://github.com/kylemcdonald/FreeWifi

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-netaddr@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-spoofmac@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-wireless@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
