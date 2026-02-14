PORTNAME=	python-stix2-patterns
DISTVERSION=	1.3.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Validate STIX 2 Patterns.
WWW=		https://github.com/oasis-open/cti-pattern-validator

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-antlr4@${PY_FLAVOR} \
		??/py-typing@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
