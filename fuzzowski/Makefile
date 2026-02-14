PORTNAME=	fuzzowski
DISTVERSION=	41.e39f665
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Network Protocol Fuzzer made by NCCGroup based on Sulley and BooFuzz.
WWW=		https://github.com/nccgroup/fuzzowski

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/py-attrs@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pydot@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
