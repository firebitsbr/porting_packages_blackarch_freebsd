PORTNAME=	detect-secrets
DISTVERSION=	v1.5.0.r49.g50119d6
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An enterprise friendly way of detecting and preventing secrets in code.
WWW=		https://github.com/Yelp/detect-secrets

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/gibberish-detector \
		??/py-ahocorasick@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
