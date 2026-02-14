PORTNAME=	doozer
DISTVERSION=	9.5cfc8f8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Password cracking utility.
WWW=		https://github.com/CoalfireLabs/crackHOR

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/hashcat \
		??/ophcrack \
		??/py-django@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
