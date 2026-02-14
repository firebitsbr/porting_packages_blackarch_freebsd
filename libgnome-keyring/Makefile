PORTNAME=	libgnome-keyring
DISTVERSION=	3.12.0.r14.g23438cc
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	GNOME keyring client library (deprecated).
WWW=		https://gitlab.gnome.org/Archive/libgnome-keyring

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/gnome-common \
		??/gobject-introspection \
		??/intltool \
		??/vala \
		devel/git

RUN_DEPENDS=	??/dbus \
		??/glib2 \
		??/libgcrypt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
