PORTNAME=	ibrute
DISTVERSION=	12.3a6a11e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An AppleID password bruteforce tool. It uses Find My Iphone service API, where bruteforce protection was not implemented.
WWW=		https://github.com/hackappcom/ibrute/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-lxml@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
