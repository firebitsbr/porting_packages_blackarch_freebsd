PORTNAME=	osueta
DISTVERSION=	82.2ee8068
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A simple Python script to exploit the OpenSSH User Enumeration Timing Attack.
WWW=		https://github.com/c0r3dump3d/osueta

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-ipy@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
