PORTNAME=	abuse-ssl-bypass-waf
DISTVERSION=	7.c28f98e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Bypassing WAF by abusing SSL/TLS Ciphers.
WWW=		https://github.com/LandGrey/abuse-ssl-bypass-waf

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/sslscan \
		ftp/curl \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
