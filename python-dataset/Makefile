PORTNAME=	python-dataset
DISTVERSION=	1.6.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Toolkit for Python-based data processing.
WWW=		https://pypi.org/project/dataset/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-alembic@${PY_FLAVOR} \
		??/py-normality@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
