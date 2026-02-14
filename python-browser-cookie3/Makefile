PORTNAME=	python-browser-cookie3
DISTVERSION=	0.20.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Loads cookies from your browser into a cookiejar object.
WWW=		https://pypi.org/project/browser-cookie3/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-lz4@${PY_FLAVOR} \
		??/py-pbkdf2@${PY_FLAVOR} \
		??/py-pyaes@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		??/py-secretstorage@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
