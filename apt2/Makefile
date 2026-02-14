PORTNAME=	apt2
DISTVERSION=	v1.0.20180315.r12.g8075cdc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automated penetration toolkit.
WWW=		https://github.com/MooseDojo/apt2

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-msgpack@${PY_FLAVOR} \
		??/py-unqlite@${PY_FLAVOR} \
		??/py-yattag@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
