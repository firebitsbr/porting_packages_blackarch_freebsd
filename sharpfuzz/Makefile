PORTNAME=	sharpfuzz
DISTVERSION=	v2.2.0.r6.gfee8d5e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	AFL-based fuzz testing for .NET.
WWW=		https://github.com/Metalnem/sharpfuzz

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/dotnet-sdk \
		devel/git

RUN_DEPENDS=	??/afl++ \
		??/dotnet-runtime


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
