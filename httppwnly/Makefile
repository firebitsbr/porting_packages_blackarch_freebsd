PORTNAME=	httppwnly
DISTVERSION=	47.528a664
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Repeater style XSS post-exploitation tool for mass browser control.
WWW=		https://github.com/Danladi/HttpPwnly

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-flask-bcrypt@${PY_FLAVOR} \
		??/py-flask-cors@${PY_FLAVOR} \
		??/py-flask-login@${PY_FLAVOR} \
		??/py-flask-socketio@${PY_FLAVOR} \
		??/py-flask-sqlalchemy@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-pysqlite@${PY_FLAVOR} \
		??/py-socketio@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
