PORTNAME=	weebdns
DISTVERSION=	14.c01c04f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	DNS Enumeration with Asynchronicity.
WWW=		https://github.com/WeebSec/weebdns

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-asyncio@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
