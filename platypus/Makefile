PORTNAME=	platypus
DISTVERSION=	v1.5.1.r204.g0cb1673
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A modern multiple reverse shell sessions manager written in go.
WWW=		https://github.com/WangYihang/Platypus

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/go-bindata \
		??/yarn \
		devel/git \
		lang/go \
		lang/python \
		www/node

RUN_DEPENDS=	??/axel \
		??/unarchiver \
		??/upx


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
