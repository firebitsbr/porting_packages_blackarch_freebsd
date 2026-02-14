PORTNAME=	sulley
DISTVERSION=	1.0.bff0dd1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A pure-python fully automated and unattended fuzzing framework.
WWW=		https://github.com/OpenRCE/sulley/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/py-pcapy@${PY_FLAVOR} \
		lang/python3 \
		net/libpcap


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
