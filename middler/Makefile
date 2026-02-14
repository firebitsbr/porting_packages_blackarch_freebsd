PORTNAME=	middler
DISTVERSION=	1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Man in the Middle tool to demonstrate protocol middling attacks.
WWW=		https://code.google.com/archive/p/middler/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	lang/python3

RUN_DEPENDS=	lang/python3 \
		net/libdnet \
		net/libpcap \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
