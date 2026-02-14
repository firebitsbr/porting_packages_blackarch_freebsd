PORTNAME=	pinkerton
DISTVERSION=	1.7.r6.gec6b954
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	JavaScript file crawler and secret finder.
WWW=		https://github.com/oppsec/Pinkerton

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-jsbeautifier@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		lang/python \
		security/openssl \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
