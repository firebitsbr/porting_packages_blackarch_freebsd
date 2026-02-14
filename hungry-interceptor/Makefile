PORTNAME=	hungry-interceptor
DISTVERSION=	391.1aea7f3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Intercepts data, does something with it, stores it.
WWW=		https://github.com/nbuechler/hungry-interceptor

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-flask-cors@${PY_FLAVOR} \
		??/py-flask-pymongo@${PY_FLAVOR} \
		??/py-flask-wtf@${PY_FLAVOR} \
		??/py-py2neo@${PY_FLAVOR} \
		??/py-pymongo@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
