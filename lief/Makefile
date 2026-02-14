PORTNAME=	lief
DISTVERSION=	0.17.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Library to instrument executable formats.
WWW=		https://github.com/lief-project/lief

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/ninja \
		??/nlohmann-json \
		??/py-build@${PY_FLAVOR} \
		??/py-cattrs@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-pathspec@${PY_FLAVOR} \
		??/py-pydantic-core@${PY_FLAVOR} \
		??/py-pydantic@${PY_FLAVOR} \
		??/py-pyproject-metadata@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-scikit-build-core@${PY_FLAVOR} \
		??/py-tomli@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python

RUN_DEPENDS=	??/tl-expected


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
