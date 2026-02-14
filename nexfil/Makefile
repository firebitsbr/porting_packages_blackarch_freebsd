PORTNAME=	nexfil
DISTVERSION=	54.c540238
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OSINT tool for finding profiles by username.
WWW=		https://github.com/thewhiteh4t/nexfil

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-aiodns@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-cchardet@${PY_FLAVOR} \
		??/py-tldextract@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
