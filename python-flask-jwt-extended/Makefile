PORTNAME=	python-flask-jwt-extended
DISTVERSION=	4.7.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Extended JSON Web Tokens (JWT) support for Flask.
WWW=		https://pypi.org/project/Flask-JWT-Extended/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-black@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-pallets-sphinx-themes@${PY_FLAVOR} \
		??/py-pre-commit@${PY_FLAVOR} \
		??/py-pyjwt@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		??/py-tox@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
