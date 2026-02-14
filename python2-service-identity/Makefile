PORTNAME=	python2-service-identity
DISTVERSION=	18.1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Service identity verification for pyOpenSSL & cryptography.
WWW=		https://pypi.org/project/service_identity/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-attrs@${PY_FLAVOR} \
		??/py-ipaddress@${PY_FLAVOR} \
		??/py-pyasn1-modules@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
