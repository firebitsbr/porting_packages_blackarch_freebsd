PORTNAME=	nsntrace
DISTVERSION=	82.ed3532e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Perform network trace of a single process by using network namespaces.
WWW=		https://github.com/jonasdn/nsntrace

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/automake \
		devel/git

RUN_DEPENDS=	??/dbus \
		??/docbook-xsl \
		??/iptables \
		??/libgcrypt \
		??/libgpg-error \
		??/libnl \
		??/libsystemd \
		??/libusb \
		??/lz4 \
		??/xz \
		net/libpcap \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
