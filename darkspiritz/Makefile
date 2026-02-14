PORTNAME=	darkspiritz
DISTVERSION=	6.4d23e94
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A penetration testing framework for Linux, MacOS, and Windows systems.
WWW=		https://github.com/M4cs/DarkSpiritz

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pycryptodomex@${PY_FLAVOR} \
		??/py-pysmb@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		lang/python \
		net/py-scapy@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
