PORTNAME=	python2-oscrypto
DISTVERSION=	1.2.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	TLS (SSL) sockets, key generation, encryption, decryption, signing, verification and KDFs using the OS crypto libraries.
WWW=		https://pypi.org/project/oscrypto/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-asn1crypto@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
