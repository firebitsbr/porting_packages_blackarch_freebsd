PORTNAME=	cloud-buster
DISTVERSION=	194.b55e4a1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool that checks Cloudflare enabled sites for origin IP leaks.
WWW=		https://github.com/SageHack/cloud-buster

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-dnspython@${PY_FLAVOR} \
		lang/python \
		security/openssl \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
