PORTNAME=	python2-cachecontrol
DISTVERSION=	0.12.6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	httplib2 caching for requests.
WWW=		https://pypi.org/project/CacheControl/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-msgpack@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
