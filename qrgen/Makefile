PORTNAME=	qrgen
DISTVERSION=	37.82a015b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple script for generating Malformed QRCodes.
WWW=		https://github.com/h0nus/QRGen

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pillow@${PY_FLAVOR} \
		??/py-qrcode@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
