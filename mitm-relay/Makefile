PORTNAME=	mitm-relay
DISTVERSION=	40.1b74741
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Hackish way to intercept and modify non-HTTP protocols through Burp & others.
WWW=		https://github.com/jrmdev/mitm_relay

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
