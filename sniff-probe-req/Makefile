PORTNAME=	sniff-probe-req
DISTVERSION=	v0.8.0.r29.g0dacf88
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Wi-Fi Probe Requests Sniffer.
WWW=		https://github.com/SkypLabs/sniff-probe-req

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-netaddr@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
