PORTNAME=	massbleed
DISTVERSION=	20.44b7e85
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	SSL Vulnerability Scanner.
WWW=		https://github.com/1N3/Sn1per

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/sslscan \
		??/testssl.sh \
		??/unicornscan \
		lang/python \
		security/nmap \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
