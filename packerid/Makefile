PORTNAME=	packerid
DISTVERSION=	16.bc54e6d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script which uses a PEiD database to identify which packer (if any) is being used by a binary.
WWW=		https://github.com/sooshie/packerid

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/capstone \
		??/py-pefile@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
