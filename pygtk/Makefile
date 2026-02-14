PORTNAME=	pygtk
DISTVERSION=	2.24.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python bindings for the GTK widget set.
WWW=		http://www.pygtk.org/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-numpy@${PY_FLAVOR} \
		??/pygobject2-devel

RUN_DEPENDS=	??/libglade \
		??/py-cairo@${PY_FLAVOR} \
		??/py-gobject2@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
