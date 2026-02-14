PORTNAME=	reconnoitre
DISTVERSION=	1.r338.gf62afba
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A security tool for multithreaded information gathering and service enumeration.
WWW=		https://github.com/codingo/Reconnoitre

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/nbtscan \
		??/net-snmp \
		lang/python \
		security/nmap \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
