PORTNAME=	kickthemout
DISTVERSION=	212.861aea2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Kick devices off your network by performing an ARP Spoof attack.
WWW=		https://github.com/k4m4/kickthemout

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/kamene \
		??/py-nmap@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
