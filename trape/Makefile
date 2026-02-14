PORTNAME=	trape
DISTVERSION=	132.6baae24
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	People tracker on the Internet: OSINT analysis and research tool by Jose Pino.
WWW=		https://github.com/jofpin/trape

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-engineio@${PY_FLAVOR} \
		??/py-eventlet@${PY_FLAVOR} \
		??/py-flask-cors@${PY_FLAVOR} \
		??/py-flask-login@${PY_FLAVOR} \
		??/py-flask-socketio@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-socketio@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
