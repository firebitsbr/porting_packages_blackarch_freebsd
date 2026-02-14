PORTNAME=	bbqsql
DISTVERSION=	261.b9859d2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	SQL injection exploit tool.
WWW=		https://github.com/neohapsis/bbqsql

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-configparser@${PY_FLAVOR} \
		??/py-eventlet@${PY_FLAVOR} \
		??/py-gevent@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
