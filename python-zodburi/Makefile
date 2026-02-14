PORTNAME=	python-zodburi
DISTVERSION=	3.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A library which parses URIs and converts them to ZODB storage objects and database arguments.
WWW=		https://pypi.org/project/zodburi/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-zconfig@${PY_FLAVOR} \
		??/py-zeo@${PY_FLAVOR} \
		??/py-zodb@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
