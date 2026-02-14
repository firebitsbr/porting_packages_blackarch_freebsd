PORTNAME=	zulucrypt
DISTVERSION=	7.1.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Front end to cryptsetup and tcplay and it allows easy management of encrypted block devices.
WWW=		https://github.com/mhogomchungu/zuluCrypt

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake

RUN_DEPENDS=	??/cryptsetup \
		??/libpwquality \
		??/libsecret \
		??/libxkbcommon-x11 \
		??/qt5-base \
		??/util-linux


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
