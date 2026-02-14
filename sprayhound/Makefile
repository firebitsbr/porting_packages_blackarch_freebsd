PORTNAME=	sprayhound
DISTVERSION=	0.0.3
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Password spraying tool and Bloodhound integration.
WWW=		https://github.com/Hackndo/sprayhound

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-ldap@${PY_FLAVOR} \
		??/py-neo4j-driver@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
