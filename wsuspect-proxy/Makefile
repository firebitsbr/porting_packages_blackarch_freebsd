PORTNAME=	wsuspect-proxy
DISTVERSION=	24.89f9375
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for MITMing insecure WSUS connections.
WWW=		https://github.com/ctxis/wsuspect-proxy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-lxml@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
