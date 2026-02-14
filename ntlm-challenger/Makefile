PORTNAME=	ntlm-challenger
DISTVERSION=	8.bd61ef6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Parse NTLM over HTTP challenge messages.
WWW=		https://github.com/b17zr/ntlm_challenger

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/impacket \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
