PORTNAME=	androick
DISTVERSION=	8.522cfb4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A python tool to help in forensics analysis on android.
WWW=		https://github.com/Flo354/Androick

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/android-sdk \
		??/android-sdk-build-tools \
		??/android-sdk-platform-tools \
		??/py-magic@${PY_FLAVOR} \
		??/sqlite \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
