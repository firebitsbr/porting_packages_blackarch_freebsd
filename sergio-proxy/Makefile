PORTNAME=	sergio-proxy
DISTVERSION=	20.8a91bb4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A multi-threaded transparent HTTP proxy for manipulating web traffic.
WWW=		https://github.com/supernothing/sergio-proxy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-constantly@${PY_FLAVOR} \
		??/py-pyopenssl@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
