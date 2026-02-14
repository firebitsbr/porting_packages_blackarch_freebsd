PORTNAME=	python2-pyopenssl
DISTVERSION=	21.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python wrapper module around the OpenSSL library.
WWW=		https://pypi.org/project/pyOpenSSL/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cryptography@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
