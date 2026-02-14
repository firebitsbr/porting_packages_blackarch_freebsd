PORTNAME=	injectus
DISTVERSION=	12.3c01fa0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	CRLF and open redirect fuzzer.
WWW=		https://github.com/BountyStrike/Injectus

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-aiofiles@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
