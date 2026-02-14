PORTNAME=	snare
DISTVERSION=	188.b17fdfe
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Super Next generation Advanced Reactive honeypot.
WWW=		https://github.com/mushorg/snare

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-aiohttp-jinja2@${PY_FLAVOR} \
		??/py-aiohttp@${PY_FLAVOR} \
		??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-cssutils@${PY_FLAVOR} \
		??/py-gitpython@${PY_FLAVOR} \
		??/py-pycodestyle@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
