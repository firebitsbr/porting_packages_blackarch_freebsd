PORTNAME=	mooscan
DISTVERSION=	10.82963b0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A scanner for Moodle LMS.
WWW=		https://github.com/vortexau/mooscan

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-gitpython@${PY_FLAVOR} \
		??/py-pytest@${PY_FLAVOR} \
		??/py-sqlalchemy@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
