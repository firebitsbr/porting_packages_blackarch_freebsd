PORTNAME=	stews
DISTVERSION=	1.0.0.r7.gc7bba5a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Security Tool for Enumerating WebSockets.
WWW=		https://github.com/PalindromeLabs/STEWS

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-cprint@${PY_FLAVOR} \
		??/py-websocket-client@${PY_FLAVOR} \
		??/zgrab \
		lang/python \
		shells/bash \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
