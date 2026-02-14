PORTNAME=	limeaide
DISTVERSION=	v2.0.0.r3.gce3c9b7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Remotely dump RAM of a Linux client and create a volatility profile for later analysis on your local host.
WWW=		https://github.com/kd8bny/LiMEaide

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-paramiko@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
