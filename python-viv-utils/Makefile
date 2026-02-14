PORTNAME=	python-viv-utils
DISTVERSION=	0.8.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Utilities for binary analysis using vivisect.
WWW=		https://pypi.org/project/viv-utils/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/mypy \
		??/py-black@${PY_FLAVOR} \
		??/py-build@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-cxxfilt@${PY_FLAVOR} \
		??/py-flirt@${PY_FLAVOR} \
		??/py-funcy@${PY_FLAVOR} \
		??/py-iniconfig@${PY_FLAVOR} \
		??/py-intervaltree@${PY_FLAVOR} \
		??/py-isort@${PY_FLAVOR} \
		??/py-msgpack@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pathspec@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-platformdirs@${PY_FLAVOR} \
		??/py-pluggy@${PY_FLAVOR} \
		??/py-pyasn1-modules@${PY_FLAVOR} \
		??/py-pyasn1@${PY_FLAVOR} \
		??/py-pycodestyle@${PY_FLAVOR} \
		??/py-pycparser@${PY_FLAVOR} \
		??/py-pyproject-hooks@${PY_FLAVOR} \
		??/py-pytest-instafail@${PY_FLAVOR} \
		??/py-pytest-sugar@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-sortedcontainers@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/vivisect \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
