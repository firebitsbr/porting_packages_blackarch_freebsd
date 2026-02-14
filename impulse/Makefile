PORTNAME=	impulse
DISTVERSION=	79.592a91b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Modern Denial-of-service ToolKit.
WWW=		https://github.com/LimerBoy/Impulse

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		??/py-phonenumbers@${PY_FLAVOR} \
		??/py-wget@${PY_FLAVOR} \
		??/scapy \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
