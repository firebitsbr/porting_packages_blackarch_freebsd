PORTNAME=	eapeak
DISTVERSION=	130.9550d1c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Analysis Suite For EAP Enabled Wireless Networks.
WWW=		https://github.com/securestate/eapeak

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-m2crypto@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
