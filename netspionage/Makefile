PORTNAME=	netspionage
DISTVERSION=	99.c24f995
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Network Forensics CLI utility that performs Network Scanning, OSINT, and Attack Detection.
WWW=		https://github.com/ANG13T/netspionage

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-pandas@${PY_FLAVOR} \
		??/py-pick@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
