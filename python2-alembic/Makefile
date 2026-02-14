PORTNAME=	python2-alembic
DISTVERSION=	1.4.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A database migration tool for SQLAlchemy.
WWW=		https://pypi.org/project/alembic/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dateutil@${PY_FLAVOR} \
		??/py-editor@${PY_FLAVOR} \
		??/py-mako@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
