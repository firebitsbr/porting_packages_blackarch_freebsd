PORTNAME=	device-pharmer
DISTVERSION=	40.b06a460
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Opens 1K+ IPs or Shodan search results and attempts to login.
WWW=		https://github.com/DanMcInerney/device-pharmer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		??/py-mechanize@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
