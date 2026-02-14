PORTNAME=	python2-recommonmark
DISTVERSION=	0.6.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A docutils-compatibility bridge to CommonMark, enabling you to write CommonMark inside of Docutils & Sphinx projects.
WWW=		https://pypi.org/project/recommonmark/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-commonmark@${PY_FLAVOR} \
		??/py-docutils@${PY_FLAVOR} \
		??/py-sphinx@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
