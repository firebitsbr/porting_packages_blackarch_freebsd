PORTNAME=	mitm
DISTVERSION=	8.bd2b351
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A simple yet effective python3 script to perform DNS spoofing via ARP poisoning.
WWW=		https://github.com/Th3Hurrican3/mitm

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-netifaces@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		??/scapy \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
