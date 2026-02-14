PORTNAME=	python-aiocache
DISTVERSION=	0.12.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Asyncio cache supporting multiple backends (memory,redis and memcached).
WWW=		https://pypi.org/project/aiocache/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-msgpack@${PY_FLAVOR} \
		??/py-ujson@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
