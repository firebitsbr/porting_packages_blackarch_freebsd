PORTNAME=	adaptix-c2
DISTVERSION=	727.6605760
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Extensible post-exploitation and adversarial emulation framework.
WWW=		https://github.com/Adaptix-Framework/AdaptixC2

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/mingw-w64-gcc \
		devel/git \
		lang/go

RUN_DEPENDS=	??/libcap \
		??/libusb \
		??/qt6-base \
		??/qt6-declarative \
		??/qt6-scxml \
		??/qt6-websockets \
		??/zlib \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
