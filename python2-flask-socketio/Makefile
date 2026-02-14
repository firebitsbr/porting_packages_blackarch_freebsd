PORTNAME=	python2-flask-socketio
DISTVERSION=	4.2.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Socket.IO integration for Flask applications.
WWW=		https://pypi.org/project/Flask-SocketIO/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-eventlet@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-socketio@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
