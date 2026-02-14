PORTNAME=	espionage
DISTVERSION=	48.2d57edd
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Network Packet and Traffic Interceptor For Linux. Sniff All Data Sent Through a Network.
WWW=		https://github.com/josh0xA/Espionage

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-httpcap@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
