PORTNAME=	firebaseenum
DISTVERSION=	19.1cbd19c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool to mass analyse potentially exposed Firebase databases on Android apps.
WWW=		https://github.com/Sambal0x/firebaseEnum

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-bs4@${PY_FLAVOR} \
		??/py-requests-futures@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
