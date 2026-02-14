PORTNAME=	threatspec
DISTVERSION=	0.5.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Project to integrate threat modelling into development process.
WWW=		https://github.com/threatspec/threatspec

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-wheel@${PY_FLAVOR} \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-click@${PY_FLAVOR} \
		??/py-comment-parser@${PY_FLAVOR} \
		??/py-graphviz@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		??/py-jsonschema@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
