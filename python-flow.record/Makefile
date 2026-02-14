PORTNAME=	python-flow.record
DISTVERSION=	3.21.r6.g6681385
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Recordization library.
WWW=		https://github.com/fox-it/flow.record

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-setuptools-scm@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/elasticsearch \
		??/httpx \
		??/lz4 \
		??/py-maxminddb@${PY_FLAVOR} \
		??/py-msgpack@${PY_FLAVOR} \
		??/py-zstandard@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
