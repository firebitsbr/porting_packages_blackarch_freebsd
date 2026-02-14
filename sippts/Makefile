PORTNAME=	sippts
DISTVERSION=	v4.1.2.r4.g57d7f8d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Set of tools to audit SIP based VoIP Systems.
WWW=		https://github.com/Pepelux/sippts

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-arpspoof@${PY_FLAVOR} \
		??/py-ipy@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pyradamsa@${PY_FLAVOR} \
		??/py-pyshark@${PY_FLAVOR} \
		??/py-rel@${PY_FLAVOR} \
		??/py-websocket-client@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
