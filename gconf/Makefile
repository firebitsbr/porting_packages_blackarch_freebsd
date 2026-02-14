PORTNAME=	gconf
DISTVERSION=	3.2.6+11+g07808097
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An obsolete configuration database system.
WWW=		https://projects-old.gnome.org/gconf/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/gnome-common \
		??/gobject-introspection \
		??/gtk-doc \
		??/intltool \
		devel/git

RUN_DEPENDS=	??/dbus-glib \
		??/libldap \
		??/libxml2 \
		??/polkit \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
