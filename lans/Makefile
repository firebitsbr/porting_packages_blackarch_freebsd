PORTNAME=	lans
DISTVERSION=	148.9f8ef2d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Multithreaded asynchronous packet parsing/injecting arp spoofer.
WWW=		https://github.com/DanMcInerney/LANs.py

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/aircrack-ng \
		??/nbtscan \
		??/py-nfqueue@${PY_FLAVOR} \
		??/py-twistedx@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
