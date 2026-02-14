PORTNAME=	ipv4bypass
DISTVERSION=	26.844d2d8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Using IPv6 to Bypass Security.
WWW=		https://github.com/milo2012/ipv4Bypass

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/arp-scan \
		??/py-nmap@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python3 \
		security/nmap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
