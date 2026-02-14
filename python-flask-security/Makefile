PORTNAME=	python-flask-security
DISTVERSION=	3.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Quick and simple security for Flask applications
WWW=		https://github.com/mattupstate/flask-security

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-flask-babelex@${PY_FLAVOR} \
		??/py-flask-login@${PY_FLAVOR} \
		??/py-flask-mail@${PY_FLAVOR} \
		??/py-flask-principal@${PY_FLAVOR} \
		??/py-flask-wtf@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-passlib@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-email-validator@${PY_FLAVOR} \
		??/py-flask-babelex@${PY_FLAVOR} \
		??/py-flask-login@${PY_FLAVOR} \
		??/py-flask-mail@${PY_FLAVOR} \
		??/py-flask-principal@${PY_FLAVOR} \
		??/py-flask-wtf@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-itsdangerous@${PY_FLAVOR} \
		??/py-passlib@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
