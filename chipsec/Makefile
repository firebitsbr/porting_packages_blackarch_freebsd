PORTNAME=	chipsec
DISTVERSION=	2.0.0.r7.g5bb516e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Platform Security Assessment Framework.
WWW=		https://github.com/chipsec/chipsec

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/linux-headers \
		devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/dkms \
		??/libelf \
		??/nasm \
		??/py-lxml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
