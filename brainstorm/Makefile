PORTNAME=	brainstorm
DISTVERSION=	36.55e6496
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A smarter web fuzzing tool that combines local LLM models and ffuf to optimize directory and file discovery.
WWW=		https://github.com/s7x/brainstorm

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/ffuf \
		??/ollama \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
