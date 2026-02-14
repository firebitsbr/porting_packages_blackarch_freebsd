PORTNAME=	rshack
DISTVERSION=	64.cf197e3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python tool which allows to carry out some attacks on RSA, and offer a few tools to manipulate RSA keys.
WWW=		https://github.com/zweisamkeit/RSHack

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-cryptography@${PY_FLAVOR} \
		??/py-gmpy2@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-rsa@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
