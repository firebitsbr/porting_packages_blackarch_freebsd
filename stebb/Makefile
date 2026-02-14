PORTNAME=	stebb
DISTVERSION=	1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	OWASP STeBB (Security Testing Browser Bundle ) is an open source Linux based penetration testing browser bundle built over Mozilla Firefox, with a vast array of tools
WWW=		http://www.stebb.com/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/diffutils \
		??/gstreamer0.10-base \
		??/imake \
		??/inetutils \
		??/libpulse \
		??/mesa \
		??/xorg-server-xvfb \
		??/yasm \
		??/zip \
		archivers/unzip \
		lang/python3

RUN_DEPENDS=	??/alsa-lib \
		??/dbus-glib \
		??/desktop-file-utils \
		??/gtk2 \
		??/hicolor-icon-theme \
		??/hunspell \
		??/libevent \
		??/libvpx \
		??/libxt \
		??/mime-types \
		??/mozilla-common \
		??/nss \
		??/sqlite \
		??/startup-notification


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
