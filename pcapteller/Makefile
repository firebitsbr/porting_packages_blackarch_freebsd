PORTNAME=	pcapteller
DISTVERSION=	1.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool designed for traffic manipulation and replay.
WWW=		https://www.encripto.no/nb/downloads/tools/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ipcalc@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
