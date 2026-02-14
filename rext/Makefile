PORTNAME=	rext
DISTVERSION=	63.5f0f626
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Router EXploitation Toolkit - small toolkit for easy creation and usage of various python scripts that work with embedded devices.
WWW=		https://github.com/j91321/rext

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-requestsexceptions@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
