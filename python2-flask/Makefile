PORTNAME=	python2-flask
DISTVERSION=	1.1.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A simple framework for building complex web applications.
WWW=		https://pypi.org/project/Flask/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
