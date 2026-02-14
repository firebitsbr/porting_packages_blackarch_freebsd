PORTNAME=	doork
DISTVERSION=	6.90c7260
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Passive Vulnerability Auditor.
WWW=		https://github.com/AeonDave/doork

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-django@${PY_FLAVOR} \
		??/py-simplejson@${PY_FLAVOR} \
		??/py-xgoogle@${PY_FLAVOR} \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
