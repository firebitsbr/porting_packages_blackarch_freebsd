PORTNAME=	gsmevil2
DISTVERSION=	12.eb96b4f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python web-based tool which use for capturing imsi numbers and sms.
WWW=		https://github.com/ninjhacks/gsmevil2

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/gr-gsm \
		??/kalibrate-rtl \
		??/py-appdirs@${PY_FLAVOR} \
		??/py-flask-socketio@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-pyshark@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
