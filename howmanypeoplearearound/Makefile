PORTNAME=	howmanypeoplearearound
DISTVERSION=	123.b05e06a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Count the number of people around you by monitoring wifi signals.
WWW=		https://github.com/schollz/howmanypeoplearearound

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-pick@${PY_FLAVOR} \
		??/wireshark-cli \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
