PORTNAME=	whispers
DISTVERSION=	2.4.0.r0.g24ee0f0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Identify hardcoded secrets in static structured text.
WWW=		https://github.com/adeptex/whispers/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-astroid@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-crossplane@${PY_FLAVOR} \
		??/py-jellyfish@${PY_FLAVOR} \
		??/py-jproperties@${PY_FLAVOR} \
		??/py-luhn@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
