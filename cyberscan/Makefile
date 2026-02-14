PORTNAME=	cyberscan
DISTVERSION=	75.ca85794
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Network Pentesting Tool.
WWW=		https://github.com/medbenali/CyberScan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-pygeoip@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
