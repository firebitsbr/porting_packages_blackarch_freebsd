PORTNAME=	python2-pynacl
DISTVERSION=	1.3.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python binding to the Networking and Cryptography (NaCl) library.
WWW=		https://pypi.org/project/PyNaCl/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/libsodium \
		??/py-cffi@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
