PORTNAME=	drupwn
DISTVERSION=	1.0.4.r2.g8186732
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Drupal enumeration & exploitation tool.
WWW=		https://github.com/immunIT/drupwn

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pysocks@${PY_FLAVOR} \
		??/py-veryprettytable@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
