PORTNAME=	python-updog
DISTVERSION=	2.0.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A replacement for Pythons SimpleHTTPServer.
WWW=		https://pypi.org/project/updog/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-poetry@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-flask-cors@${PY_FLAVOR} \
		??/py-flask-httpauth@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
