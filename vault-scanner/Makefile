PORTNAME=	vault-scanner
DISTVERSION=	299.0303cf4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Swiss army knife for hackers.
WWW=		https://github.com/abhisharma404/vault

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-htmlparser@${PY_FLAVOR} \
		??/py-ipwhois@${PY_FLAVOR} \
		??/py-nmap@${PY_FLAVOR} \
		??/py-pynput@${PY_FLAVOR} \
		??/scapy \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
