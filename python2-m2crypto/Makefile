PORTNAME=	python2-m2crypto
DISTVERSION=	0.38.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python crypto and SSL toolkit.
WWW=		https://pypi.org/project/M2Crypto/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/swig \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-typing@${PY_FLAVOR} \
		lang/python3 \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
