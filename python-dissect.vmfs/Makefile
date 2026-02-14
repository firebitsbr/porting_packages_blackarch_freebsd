PORTNAME=	python-dissect.vmfs
DISTVERSION=	3.13.r0.ga7e4b6b
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Dissect module implementing a parser for the VMFS file system, used by VMware virtualization software.
WWW=		https://github.com/fox-it/dissect.vmfs

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-setuptools-scm@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dissect.cstruct@${PY_FLAVOR} \
		??/py-dissect.util@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
