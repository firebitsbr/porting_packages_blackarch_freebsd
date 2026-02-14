PORTNAME=	omnihash
DISTVERSION=	70.870e9ae
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Hash files, strings, input streams and network resources in various common algorithms simultaneously.
WWW=		https://github.com/Miserlou/omnihash

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-certifi@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-crcmod@${PY_FLAVOR} \
		??/py-pyblake2@${PY_FLAVOR} \
		??/py-sha3@${PY_FLAVOR} \
		??/py-validators@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
