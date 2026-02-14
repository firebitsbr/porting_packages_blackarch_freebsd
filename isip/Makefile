PORTNAME=	isip
DISTVERSION=	2.fad1f10
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Interactive sip toolkit for packet manipulations, sniffing, man in the middle attacks, fuzzing, simulating of dos attacks.
WWW=		https://github.com/halitalptekin/isip

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dpkt@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-wsgiref@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
