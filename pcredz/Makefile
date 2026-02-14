PORTNAME=	pcredz
DISTVERSION=	106.200cdb0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool that extracts credit card numbers and more from a pcap file or from a live interface.
WWW=		https://github.com/lgandx/PCredz

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-libpcap@${PY_FLAVOR} \
		lang/python \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
