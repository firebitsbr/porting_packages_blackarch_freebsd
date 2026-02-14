PORTNAME=	pymssql
DISTVERSION=	2.1.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A fast MS SQL Server client library for Python directly using C API instead of ODBC. It is Python DB-API 2.0 compliant. Works on Linux, *BSD, Solaris, Mac OS X and Windows.
WWW=		https://pypi.python.org/pypi/pymssql/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/cython2 \
		??/freetds \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
