PORTNAME=	creak
DISTVERSION=	41.a6c011f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Poison, reset, spoof, redirect MITM script.
WWW=		https://github.com/codepr/creak

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dpkt@${PY_FLAVOR} \
		??/py-pydnet@${PY_FLAVOR} \
		??/py-pypcap@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
