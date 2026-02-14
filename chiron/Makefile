PORTNAME=	chiron
DISTVERSION=	48.524abe1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An all-in-one IPv6 Penetration Testing Framework.
WWW=		http://www.secfu.net/tools-scripts/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ipaddr@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
