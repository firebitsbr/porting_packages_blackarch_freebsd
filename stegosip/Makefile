PORTNAME=	stegosip
DISTVERSION=	11.5cda6d6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	TCP tunnel over RTP/SIP.
WWW=		https://github.com/epinna/Stegosip

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dpkt@${PY_FLAVOR} \
		??/py-nfqueue@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
