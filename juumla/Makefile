PORTNAME=	juumla
DISTVERSION=	106.130565e
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Python tool created to identify Joomla version, scan for vulnerabilities and search for config files.
WWW=		https://github.com/oppsec/juumla

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-rich@${PY_FLAVOR} \
		??/py-xmltodict@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
