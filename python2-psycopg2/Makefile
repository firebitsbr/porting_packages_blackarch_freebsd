PORTNAME=	python2-psycopg2
DISTVERSION=	2.8.6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A PostgreSQL database adapter for the Python programming language.
WWW=		https://pypi.org/project/psycopg2/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/postgresql-libs \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/postgresql-libs \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
