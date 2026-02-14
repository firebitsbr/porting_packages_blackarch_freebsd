PORTNAME=	netattack
DISTVERSION=	24.230b856
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python script to scan and attack wireless networks.
WWW=		https://github.com/chrizator/netattack2

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/iw \
		??/py-argparse@${PY_FLAVOR} \
		??/wireless_tools \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
