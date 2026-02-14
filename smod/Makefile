PORTNAME=	smod
DISTVERSION=	53.7eb8423
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A modular framework with every kind of diagnostic and offensive feature you could need in order to pentest modbus protocol.
WWW=		https://github.com/enddo/smod

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-archinfo@${PY_FLAVOR} \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
