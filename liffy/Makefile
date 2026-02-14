PORTNAME=	liffy
DISTVERSION=	46.b990d6a
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Local File Inclusion Exploitation tool.
WWW=		https://github.com/mzfr/liffy/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-daemon@${PY_FLAVOR} \
		??/py-pyfiglet@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
