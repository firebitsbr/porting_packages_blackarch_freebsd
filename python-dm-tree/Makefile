PORTNAME=	python-dm-tree
DISTVERSION=	0.1.9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Library for working with nested data structures.
WWW=		https://github.com/google-deepmind/tree

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/abseil-cpp \
		??/py-absl@${PY_FLAVOR} \
		??/py-attrs@${PY_FLAVOR} \
		??/py-numpy@${PY_FLAVOR} \
		??/py-wrapt@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
