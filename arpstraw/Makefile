PORTNAME=	arpstraw
DISTVERSION=	27.ab40e13
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Arp spoof detection tool.
WWW=		https://github.com/he2ss/arpstraw

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-apipkg@${PY_FLAVOR} \
		??/py-argparse@${PY_FLAVOR} \
		??/py-backports@${PY_FLAVOR} \
		??/py-configparser@${PY_FLAVOR} \
		??/py-gobject@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pyshark@${PY_FLAVOR} \
		??/py-trollius@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
