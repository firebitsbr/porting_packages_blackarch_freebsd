PORTNAME=	websockify
DISTVERSION=	988.e9bd68c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	WebSocket to TCP proxy/bridge.
WWW=		http://github.com/kanaka/websockify

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-mox3@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
