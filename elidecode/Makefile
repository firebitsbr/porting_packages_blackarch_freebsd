PORTNAME=	elidecode
DISTVERSION=	48.38fa5ba
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool to decode obfuscated shellcodes using the unicorn-engine for the emulation and the capstone-engine to print the asm code.
WWW=		https://github.com/DeveloppSoft/EliDecode

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git

RUN_DEPENDS=	??/capstone \
		??/py-argparse@${PY_FLAVOR} \
		??/py-capstone@${PY_FLAVOR} \
		??/py-unicorn@${PY_FLAVOR} \
		??/unicorn \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3 \
		shells/bash


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
