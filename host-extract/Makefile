PORTNAME=	host-extract
DISTVERSION=	8.0134ad7
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Ruby script tries to extract all IP/Host patterns in page response of a given URL and JavaScript/CSS files of that URL.
WWW=		https://code.google.com/p/host-extract/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/ruby-http-cookie \
		??/ruby-mechanize \
		??/ruby-net-http-digest_auth \
		??/ruby-ntlm-http \
		??/ruby-rubyntlm \
		??/ruby-webrick \
		??/ruby-webrobots \
		??/rubygems \
		lang/ruby


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
