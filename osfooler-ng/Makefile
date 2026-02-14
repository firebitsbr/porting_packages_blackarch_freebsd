PORTNAME=	osfooler-ng
DISTVERSION=	2.c0b20d6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Prevents remote active/passive OS fingerprinting by tools like nmap or p0f.
WWW=		https://github.com/segofensiva/OSfooler-ng

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-dpkt@${PY_FLAVOR} \
		??/py-nfqueue@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
