PORTNAME=	ssrf-proxy
DISTVERSION=	293.e79da7a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Facilitates tunneling HTTP communications through servers vulnerable to Server-Side Request Forgery.
WWW=		https://github.com/bcoles/ssrf_proxy

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/ruby-rdoc \
		devel/git

RUN_DEPENDS=	lang/ruby \
		sysutils/rubygem-bundler \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
