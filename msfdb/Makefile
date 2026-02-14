PORTNAME=	msfdb
DISTVERSION=	16.09c603b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Manage the metasploit framework database.
WWW=		https://github.com/BlackArch/msfdb

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/lsof \
		??/metasploit \
		??/postgresql \
		??/postgresql-libs \
		??/sed \
		security/openssl


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
