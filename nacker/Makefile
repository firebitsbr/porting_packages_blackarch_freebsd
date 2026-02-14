PORTNAME=	nacker
DISTVERSION=	23.b67bb39
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool to circumvent 802.1x Network Access Control on a wired LAN.
WWW=		https://github.com/carmaa/nacker

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-netaddr@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
