PORTNAME=	barf
DISTVERSION=	923.9547ef8
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A multiplatform open source Binary Analysis and Reverse engineering Framework.
WWW=		https://github.com/programa-stic/barf-project

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-pefile@${PY_FLAVOR} \
		??/py-pydot@${PY_FLAVOR} \
		??/py-pyelftools@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-ropper@${PY_FLAVOR} \
		??/ropgadget \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
