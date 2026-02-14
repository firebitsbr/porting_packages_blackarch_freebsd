PORTNAME=	holehe
DISTVERSION=	434.14da70f
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for Efficiently finding registered accounts from emails.
WWW=		https://github.com/megadose/holehe

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-beautifulsoup4@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-httpx@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		??/py-trio@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
