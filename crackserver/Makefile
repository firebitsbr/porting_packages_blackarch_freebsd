PORTNAME=	crackserver
DISTVERSION=	33.e5763ab
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An XMLRPC server for password cracking.
WWW=		https://github.com/averagesecurityguy/crack

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/hashcat \
		??/ike-scan \
		??/john \
		??/pyrit \
		??/rcracki_mt \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
