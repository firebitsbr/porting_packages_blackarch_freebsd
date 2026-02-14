PORTNAME=	imhex
DISTVERSION=	nightly.r0.gf476842
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Hex Editor for Reverse Engineers, Programmers and people that value their eye sight when working at 3 AM.
WWW=		https://github.com/WerWolv/ImHex

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/cmake \
		??/freetype2 \
		??/gcc \
		??/librsvg \
		??/lld \
		??/llvm \
		devel/git

RUN_DEPENDS=	??/capstone \
		??/dbus \
		??/file \
		??/fmt \
		??/freetype2 \
		??/glfw \
		??/glm \
		??/gtk3 \
		??/hicolor-icon-theme \
		??/libssh2 \
		??/llvm \
		??/llvm-libs \
		??/mbedtls \
		??/nlohmann-json \
		??/xdg-desktop-portal-gtk \
		??/yara \
		ftp/curl \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
