PORTNAME=	hubbit-sniffer
DISTVERSION=	74.460ecf8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Simple application that listens for WIFI-frames and records the mac-address of the sender and posts them to a REST-api.
WWW=		https://github.com/cthit/hubbIT-sniffer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
