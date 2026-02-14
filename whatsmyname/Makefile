PORTNAME=	whatsmyname
DISTVERSION=	2740.a37a2df
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool to perform user and username enumeration on various websites.
WWW=		https://github.com/WebBreacher/WhatsMyName

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-aiohttp@${PY_FLAVOR} \
		??/py-multidict@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
