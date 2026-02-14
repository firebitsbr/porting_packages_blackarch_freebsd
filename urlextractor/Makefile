PORTNAME=	urlextractor
DISTVERSION=	19.739864d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Information gathering & website reconnaissance.
WWW=		https://github.com/eschultze/URLextractor

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/bc \
		??/bind-tools \
		??/py-tldextract@${PY_FLAVOR} \
		??/whois \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
