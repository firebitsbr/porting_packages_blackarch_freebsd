PORTNAME=	nosqli-user-pass-enum
DISTVERSION=	18.1b3713a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Script to enumerate usernames and passwords from vulnerable web applications running MongoDB.
WWW=		https://github.com/an0nlk/Nosql-MongoDB-injection-username-password-enumeration

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-colorama@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
