PORTNAME=	hellraiser
DISTVERSION=	279.bea43e2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Vulnerability Scanner.
WWW=		https://github.com/m0nad/HellRaiser

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/make \
		devel/git

RUN_DEPENDS=	??/redis \
		??/ruby-foreman \
		??/ruby-pkg-config \
		??/ruby-rake \
		??/ruby2.7 \
		security/nmap \
		sysutils/rubygem-bundler \
		textproc/libxslt \
		www/node


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
