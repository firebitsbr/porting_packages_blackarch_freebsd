PORTNAME=	python-blis
DISTVERSION=	1.3.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Blis linear algebra routines as a self-contained Python C-extension.
WWW=		https://pypi.org/project/blis/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cython \
		??/py-numpy@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-hypothesis@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
