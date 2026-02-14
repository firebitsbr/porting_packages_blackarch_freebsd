PORTNAME=	boopsuite
DISTVERSION=	1.1c4e68d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Suite of Tools written in Python for wireless auditing and security testing.
WWW=		https://github.com/M1ND-B3ND3R/BoopSuite

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-argparse@${PY_FLAVOR} \
		??/py-netaddr@${PY_FLAVOR} \
		??/py-pyric@${PY_FLAVOR} \
		??/py-tabulate@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
