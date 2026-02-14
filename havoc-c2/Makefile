PORTNAME=	havoc-c2
DISTVERSION=	856.fb67b76
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Modern and malleable post-exploitation command and control framework.
WWW=		https://havocframework.com/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/qt5-websockets \
		devel/git \
		lang/go

RUN_DEPENDS=	??/bzip2 \
		??/fontconfig \
		??/gdbm \
		??/glu \
		??/gtest \
		??/libffi \
		??/mesa \
		??/mingw-w64-gcc \
		??/nasm \
		??/ncurses \
		??/qt5-base \
		??/qt5-websockets \
		??/readline \
		??/spdlog \
		??/sqlite \
		lang/python \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
