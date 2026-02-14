PORTNAME=	dradis-ce
DISTVERSION=	v4.9.0.r2424.ga4c8bbe
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An open source framework to enable effective information sharing.
WWW=		https://dradis.com/ce/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/pkgconf \
		devel/git

RUN_DEPENDS=	??/libsass \
		??/postgresql-libs \
		??/ruby-erb \
		??/sqlite \
		devel/git \
		lang/ruby \
		sysutils/rubygem-bundler \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
