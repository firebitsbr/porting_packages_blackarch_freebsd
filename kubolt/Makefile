PORTNAME=	kubolt
DISTVERSION=	28.0027239
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Utility for scanning public kubernetes clusters.
WWW=		https://github.com/averonesis/kubolt

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-shodan@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
