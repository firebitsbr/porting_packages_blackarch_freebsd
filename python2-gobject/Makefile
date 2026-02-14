PORTNAME=	python2-gobject
DISTVERSION=	3.34.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python2 Bindings for GLib/GObject/GIO/GTK+.
WWW=		https://wiki.gnome.org/Projects/PyGObject

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/gobject-introspection \
		??/meson \
		??/py-cairo@${PY_FLAVOR} \
		devel/git

RUN_DEPENDS=	??/gobject-introspection-runtime


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
