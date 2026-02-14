PORTNAME=	jwt-tool
DISTVERSION=	v2.3.0.r0.g3bc7407
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Toolkit for validating, forging and cracking JWTs (JSON Web Tokens).
WWW=		https://github.com/ticarpi/jwt_tool

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-cprint@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		??/py-ratelimit@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
