PORTNAME=	qt5-webkit
DISTVERSION=	${.pkgver/./}
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Classes for a WebKit2 based implementation and a new QML API.
WWW=		https://github.com/qtwebkit/qtwebkit

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/gperf \
		??/qt5-doc \
		??/qt5-tools \
		??/ruby-erb \
		lang/python \
		lang/ruby

RUN_DEPENDS=	??/glib2 \
		??/gst-plugins-base \
		??/gst-plugins-base-libs \
		??/gstreamer \
		??/hyphen \
		??/icu \
		??/libicui18n.so \
		??/libicuuc.so \
		??/libjpeg-turbo \
		??/libpng \
		??/libwebp \
		??/libx11 \
		??/libxcomposite \
		??/libxml2 \
		??/qt5-base \
		??/qt5-declarative \
		??/qt5-location \
		??/qt5-sensors \
		??/qt5-webchannel \
		??/sqlite \
		??/woff2 \
		??/zlib


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
