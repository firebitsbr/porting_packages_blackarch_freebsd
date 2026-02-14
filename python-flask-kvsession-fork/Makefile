PORTNAME=	python-flask-kvsession-fork
DISTVERSION=	0.6.4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Transparent server-side session support for flask.
WWW=		https://pypi.org/project/flask-kvsession-fork/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-flask@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-simplekv@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
