PORTNAME=	grammarinator
DISTVERSION=	492.7ce0711
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A random test generator / fuzzer that creates test cases according to an input ANTLR v4 grammar.
WWW=		https://github.com/renatahodovan/grammarinator

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/java-environment \
		??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/autopep8 \
		??/py-antlerinator@${PY_FLAVOR} \
		??/py-antlr4@${PY_FLAVOR} \
		??/py-jinja@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
