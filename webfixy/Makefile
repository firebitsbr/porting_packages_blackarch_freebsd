PORTNAME=	webfixy
DISTVERSION=	25.5d477b0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	On-the-fly decryption proxy for MikroTik RouterOS WebFig sessions.
WWW=		https://github.com/takeshixx/webfixy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-aiohttp@${PY_FLAVOR} \
		??/py-demjson@${PY_FLAVOR} \
		??/py-passlib@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
