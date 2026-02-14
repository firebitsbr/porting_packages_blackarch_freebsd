PORTNAME=	ipsourcebypass
DISTVERSION=	1.2.r17.gd89edb1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	This Python script can be used to bypass IP source restrictions using HTTP headers.
WWW=		https://github.com/p0dalirius/ipsourcebypass

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-rich@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
