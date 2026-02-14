PORTNAME=	sensepost-xrdp
DISTVERSION=	16.46d6c19
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A rudimentary remote desktop tool for the X11 protocol exploiting unauthenticated x11 sessions.
WWW=		https://github.com/sensepost/xrdp

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-cairo@${PY_FLAVOR} \
		??/pygtk \
		??/xdotool \
		??/xrdp \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
