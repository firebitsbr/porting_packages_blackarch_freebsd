PORTNAME=	python-face
DISTVERSION=	24.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A command-line application framework (and CLI parser).
WWW=		https://github.com/mahmoud/face

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-boltons@${PY_FLAVOR} \
		??/py-cachetools@${PY_FLAVOR} \
		??/py-chardet@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-coverage@${PY_FLAVOR} \
		??/py-distlib@${PY_FLAVOR} \
		??/py-exceptiongroup@${PY_FLAVOR} \
		??/py-filelock@${PY_FLAVOR} \
		??/py-importlib-metadata@${PY_FLAVOR} \
		??/py-iniconfig@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-platformdirs@${PY_FLAVOR} \
		??/py-pluggy@${PY_FLAVOR} \
		??/py-pyproject-api@${PY_FLAVOR} \
		??/py-pyproject-hooks@${PY_FLAVOR} \
		??/py-tomli@${PY_FLAVOR} \
		??/py-tox@${PY_FLAVOR} \
		??/py-typing_extensions@${PY_FLAVOR} \
		??/py-zipp@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
