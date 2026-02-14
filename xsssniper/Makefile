PORTNAME=	xsssniper
DISTVERSION=	79.02b59af
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An automatic XSS discovery tool
WWW=		https://github.com/gbrindisi/xsssniper

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-hgapi@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-mechanize@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
