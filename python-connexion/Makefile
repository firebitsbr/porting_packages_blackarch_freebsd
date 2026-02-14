PORTNAME=	python-connexion
DISTVERSION=	2.14.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Swagger/OpenAPI First framework for Python on top of Flask with automatic endpoint validation & OAuth2 support.
WWW=		https://github.com/zalando/connexion

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/flake8 \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-clickclick@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-importlib-metadata@${PY_FLAVOR} \
		??/py-inflection@${PY_FLAVOR} \
		??/py-jsonschema@${PY_FLAVOR} \
		??/py-openapi-spec-validator@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pyaml@${PY_FLAVOR} \
		??/py-werkzeug@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
