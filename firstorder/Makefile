PORTNAME=	firstorder
DISTVERSION=	8.107eb6a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A traffic analyzer to evade Empire communication from Anomaly-Based IDS.
WWW=		https://github.com/tearsecurity/firstorder

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-scahttp@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
