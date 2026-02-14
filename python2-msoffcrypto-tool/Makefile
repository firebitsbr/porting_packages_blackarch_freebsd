PORTNAME=	python2-msoffcrypto-tool
DISTVERSION=	5.0.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Python tool and library for decrypting MS Office files with passwords or other keys.
WWW=		https://pypi.org/project/msoffcrypto-tool/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-cryptography@${PY_FLAVOR} \
		??/py-olefile@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
