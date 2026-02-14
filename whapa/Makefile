PORTNAME=	whapa
DISTVERSION=	389.8e5beae
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	WhatsApp Parser Tool.
WWW=		https://github.com/B16f00t/whapa

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-gpsoauth@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/tk \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
