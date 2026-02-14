PORTNAME=	python-acquire
DISTVERSION=	3.21.r3.ga042049
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Quickly gather forensic artifacts from disk images or a live system into a lightweight container.
WWW=		https://github.com/fox-it/acquire

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-installer@${PY_FLAVOR} \
		??/py-setuptools-scm@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR} \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-dissect.cstruct@${PY_FLAVOR} \
		??/py-dissect.target@${PY_FLAVOR} \
		??/py-minio@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-requests-toolbelt@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
