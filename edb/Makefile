PORTNAME=	edb
DISTVERSION=	3341.bf0c1395
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A cross platform AArch32/x86/x86-64 debugger.
WWW=		https://github.com/eteran/edb-debugger/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/boost \
		??/cmake \
		??/qt5-tools \
		devel/git

RUN_DEPENDS=	??/capstone \
		??/graphviz \
		??/gtk-update-icon-cache \
		??/qt5-svg \
		??/qt5-xmlpatterns


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
