PORTNAME=	snapception
DISTVERSION=	8.c156f9e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Intercept and decrypt all snapchats received over your network.
WWW=		https://github.com/thebradbain/snapception

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/mitmproxy \
		??/py-click@${PY_FLAVOR} \
		??/py-sortedcontainers@${PY_FLAVOR} \
		lang/python3 \
		lang/ruby \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
