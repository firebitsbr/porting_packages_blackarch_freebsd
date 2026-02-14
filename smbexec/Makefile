PORTNAME=	smbexec
DISTVERSION=	59.a54fc14
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A rapid psexec style attack with samba tools.
WWW=		https://github.com/pentestgeek/smbexec

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/make \
		devel/git

RUN_DEPENDS=	??/ruby-pkg-config \
		lang/ruby \
		sysutils/rubygem-bundler \
		textproc/libxslt


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
