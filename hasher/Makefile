PORTNAME=	hasher
DISTVERSION=	48.40173c5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool that allows you to quickly hash plaintext strings, or compare hashed values with a plaintext locally.
WWW=		https://github.com/ChrisTruncer/Hasher

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-bcrypt@${PY_FLAVOR} \
		??/py-passlib@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
