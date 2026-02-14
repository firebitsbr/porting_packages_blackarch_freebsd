PORTNAME=	beef
DISTVERSION=	v0.6.0.0.r159.gfa87807
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	The Browser Exploitation Framework that focuses on the web browser.
WWW=		https://github.com/beefproject/beef

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/ruby-eventmachine \
		??/sqlite \
		lang/python \
		lang/ruby \
		sysutils/rubygem-bundler \
		textproc/libxslt \
		www/node


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
