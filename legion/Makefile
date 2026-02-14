PORTNAME=	legion
DISTVERSION=	61.ca99853
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automatic Enumeration Tool based in Open Source tools.
WWW=		https://github.com/carlospolop/legion

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/arjun \
		??/dirhunt \
		??/dirsearch \
		??/impacket \
		??/py-termcolor@${PY_FLAVOR} \
		??/rpcbind \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
