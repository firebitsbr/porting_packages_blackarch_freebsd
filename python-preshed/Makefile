PORTNAME=	python-preshed
DISTVERSION=	4.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple but high performance Cython hash table mapping pre-randomized keys to void* values.
WWW=		https://pypi.org/project/preshed/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/cython \
		??/py-cymem@${PY_FLAVOR} \
		??/py-murmurhash@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
