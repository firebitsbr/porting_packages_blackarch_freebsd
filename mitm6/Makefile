PORTNAME=	mitm6
DISTVERSION=	33.8e75884
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Pwning IPv4 via IPv6.
WWW=		https://github.com/fox-it/mitm6

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-netifaces@${PY_FLAVOR} \
		??/py-twisted@${PY_FLAVOR} \
		??/scapy \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
