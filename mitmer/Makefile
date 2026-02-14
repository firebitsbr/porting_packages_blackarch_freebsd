PORTNAME=	mitmer
DISTVERSION=	22.b01c7fe
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A man-in-the-middle and phishing attack tool that steals the victims credentials of some web services like Facebook.
WWW=		https://github.com/husam212/MITMer

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-nfqueue@${PY_FLAVOR} \
		lang/python3 \
		net/py-scapy@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
