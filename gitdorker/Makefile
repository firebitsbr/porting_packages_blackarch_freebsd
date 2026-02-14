PORTNAME=	gitdorker
DISTVERSION=	113.8199375
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python program to scrape secrets from GitHub through usage of a large repository of dorks.
WWW=		https://github.com/obheda12/GitDorker

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-termcolor@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
