PORTNAME=	sigma
DISTVERSION=	0.20
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Generic Signature Format for SIEM Systems
WWW=		https://github.com/SigmaHQ/sigma/releases

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-progressbar@${PY_FLAVOR} \
		??/py-pymisp@${PY_FLAVOR} \
		??/py-ruamel-yaml@${PY_FLAVOR} \
		??/py-urllib3@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
