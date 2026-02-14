PORTNAME=	mrsip
DISTVERSION=	110.bdd98ad
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	SIP-Based Audit and Attack Tool.
WWW=		https://github.com/meliht/mr.sip

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ipaddress@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pyfiglet@${PY_FLAVOR} \
		??/toilet \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
