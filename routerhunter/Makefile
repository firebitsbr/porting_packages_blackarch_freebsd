PORTNAME=	routerhunter
DISTVERSION=	21.4da257c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool used to find vulnerable routers and devices on the Internet and perform tests.
WWW=		https://github.com/jh00nbr/Routerhunter-2.0

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-simplejson@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
