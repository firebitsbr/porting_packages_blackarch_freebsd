PORTNAME=	elite-proxy-finder
DISTVERSION=	51.1ced3be
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Finds public elite anonymity proxies and concurrently tests them.
WWW=		https://github.com/DanMcInerney/elite-proxy-finder

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup3@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
