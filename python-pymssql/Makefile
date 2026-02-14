PORTNAME=	python-pymssql
DISTVERSION=	2.3.11
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	DB-API interface to Microsoft SQL Server for Python. (new Cython-based version).
WWW=		https://pypi.org/project/pymssql/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cython \
		??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/freetds \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
