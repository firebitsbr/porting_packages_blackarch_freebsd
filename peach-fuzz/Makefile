PORTNAME=	peach-fuzz
DISTVERSION=	55.404e8ee
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple vulnerability scanning framework.
WWW=		https://github.com/Caleb1994/peach

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-pwntools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
