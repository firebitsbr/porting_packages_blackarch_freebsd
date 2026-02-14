PORTNAME=	domained
DISTVERSION=	80.d9d079c
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Multi Tool Subdomain Enumeration.
WWW=		https://github.com/TypeError/domained

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/amass \
		??/knock \
		??/ldns \
		??/massdns \
		??/py-colorama@${PY_FLAVOR} \
		??/recon-ng \
		??/subbrute \
		??/subfinder \
		??/sublist3r \
		lang/go \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
