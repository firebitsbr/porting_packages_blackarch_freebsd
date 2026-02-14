PORTNAME=	unblob
DISTVERSION=	25.11.25.r109.g5d1ad81
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Extract files from any kind of container formats.
WWW=		https://github.com/onekey-sec/unblob

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/jefferson \
		??/py-arpy@${PY_FLAVOR} \
		??/py-attrs@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-cryptography@${PY_FLAVOR} \
		??/py-dissect.cstruct@${PY_FLAVOR} \
		??/py-lark@${PY_FLAVOR} \
		??/py-lief@${PY_FLAVOR} \
		??/py-lz4@${PY_FLAVOR} \
		??/py-magic@${PY_FLAVOR} \
		??/py-plotext@${PY_FLAVOR} \
		??/py-pluggy@${PY_FLAVOR} \
		??/py-pydantic@${PY_FLAVOR} \
		??/py-pyfatfs@${PY_FLAVOR} \
		??/py-pymdown-extensions@${PY_FLAVOR} \
		??/py-pyperscan@${PY_FLAVOR} \
		??/py-pyzstd@${PY_FLAVOR} \
		??/py-rarfile@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-structlog@${PY_FLAVOR} \
		??/py-treelib@${PY_FLAVOR} \
		??/py-ubi-reader@${PY_FLAVOR} \
		??/py-unblob-native@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
