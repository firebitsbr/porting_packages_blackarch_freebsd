PORTNAME=	clusterd
DISTVERSION=	143.d190b2c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Automates the fingerprinting, reconnaissance, and exploitation phases of an application server attack.
WWW=		https://github.com/hatRiot/clusterd

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/java-environment \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
