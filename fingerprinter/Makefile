PORTNAME=	fingerprinter
DISTVERSION=	486.e0078b4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	CMS/LMS/Library etc Versions Fingerprinter.
WWW=		https://github.com/erwanlr/Fingerprinter

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		sysutils/rubygem-bundler

RUN_DEPENDS=	??/ruby-pkg-config \
		lang/ruby \
		sysutils/rubygem-bundler \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
