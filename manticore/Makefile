PORTNAME=	manticore
DISTVERSION=	0.3.7.r82.gfe2ac40
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Symbolic execution tool.
WWW=		https://github.com/trailofbits/manticore

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-cbor2@${PY_FLAVOR} \
		??/py-crytic-compile@${PY_FLAVOR} \
		??/py-intervaltree@${PY_FLAVOR} \
		??/py-ply@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-protobuf@${PY_FLAVOR} \
		??/py-pyelftools@${PY_FLAVOR} \
		??/py-pyevmasm@${PY_FLAVOR} \
		??/py-pysha3@${PY_FLAVOR} \
		??/py-redis@${PY_FLAVOR} \
		??/py-rlp@${PY_FLAVOR} \
		??/py-unicorn@${PY_FLAVOR} \
		??/py-wasm@${PY_FLAVOR} \
		??/py-yaml@${PY_FLAVOR} \
		??/py-z3-solver@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
