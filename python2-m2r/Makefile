PORTNAME=	python2-m2r
DISTVERSION=	0.2.1
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Markdown and reStructuredText in a single file.
WWW=		https://pypi.org/project/m2r/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-docutils@${PY_FLAVOR} \
		??/py-mistune@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
