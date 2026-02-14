PORTNAME=	python-dissect.shellitem
DISTVERSION=	3.13.r0.g16bf53d
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A Dissect module implementing a parser for the Shellitem structures, commonly used by Microsoft Windows.
WWW=		https://github.com/fox-it/dissect.shellitem

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
