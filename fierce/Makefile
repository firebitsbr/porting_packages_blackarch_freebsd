PORTNAME=	fierce
DISTVERSION=	145.965840d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A DNS reconnaissance tool for locating non-contiguous IP space.
WWW=		https://github.com/mschwager/fierce

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dnspython@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
