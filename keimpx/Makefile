PORTNAME=	keimpx
DISTVERSION=	300.37190f4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Tool to verify the usefulness of credentials across a network over SMB.
WWW=		http://code.google.com/p/keimpx/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-distribute@${PY_FLAVOR} \
		devel/git

RUN_DEPENDS=	??/impacket \
		??/py-pycryptodome@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
