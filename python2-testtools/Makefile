PORTNAME=	python2-testtools
DISTVERSION=	2.3.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Extensions to the Python standard library unit testing framework.
WWW=		https://pypi.org/project/testtools/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-extras@${PY_FLAVOR} \
		??/py-mimeparse@${PY_FLAVOR} \
		??/py-pbr@${PY_FLAVOR} \
		??/py-pyrsistent@${PY_FLAVOR} \
		??/py-traceback2@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
