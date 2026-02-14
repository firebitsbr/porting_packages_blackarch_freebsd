PORTNAME=	dhcpig
DISTVERSION=	1.6.r8.gdfe9e45
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Enhanced DHCPv4 and DHCPv6 exhaustion and fuzzing script written in python using scapy network library.
WWW=		https://github.com/kamorin/DHCPig

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	lang/python \
		net/libpcap \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
