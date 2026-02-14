PORTNAME=	x3270
DISTVERSION=	4.3ga9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An IBM 3270 terminal emulator for the X Window System.
WWW=		http://x3270.bgp.nu/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/imake \
		??/libx11 \
		??/libxaw \
		??/libxt \
		??/tcl \
		??/xbitmaps \
		??/xorg-bdftopcf \
		??/xorg-mkfontdir \
		security/openssl

RUN_DEPENDS=	??/libxaw \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
