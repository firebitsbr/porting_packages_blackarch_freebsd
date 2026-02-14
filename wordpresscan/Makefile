PORTNAME=	wordpresscan
DISTVERSION=	76.f810c1c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	WPScan rewritten in Python + some WPSeku ideas.
WWW=		https://github.com/swisskyrepo/Wordpresscan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-tornado@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
