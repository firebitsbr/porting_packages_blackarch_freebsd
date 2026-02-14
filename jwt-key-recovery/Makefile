PORTNAME=	jwt-key-recovery
DISTVERSION=	11.094df95
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Recovers the public key used to sign JWT tokens.
WWW=		https://github.com/FlorianPicca/JWT-Key-Recovery

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-fastecdsa@${PY_FLAVOR} \
		??/py-gmpy2@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
