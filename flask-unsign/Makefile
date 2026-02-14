PORTNAME=	flask-unsign
DISTVERSION=	v1.2.1.r0.g6e6e91d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Command line tool to fetch, decode, brute-force and craft session cookies of a Flask application by guessing secret keys.
WWW=		https://github.com/Paradoxis/Flask-Unsign

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-flask@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-markupsafe@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
