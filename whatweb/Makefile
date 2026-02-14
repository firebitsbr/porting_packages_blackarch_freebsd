PORTNAME=	whatweb
DISTVERSION=	v0.6.3.r10.gc42e1b9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Next generation web scanner that identifies what websites are running.
WWW=		http://www.morningstarsecurity.com/research/whatweb

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/ruby-addressable \
		lang/ruby \
		sysutils/rubygem-bundler \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
