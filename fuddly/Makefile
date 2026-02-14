PORTNAME=	fuddly
DISTVERSION=	0.30.dev.r304.gaa55962
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Fuzzing and Data Manipulation Framework (for GNU/Linux).
WWW=		https://github.com/k0retux/fuddly

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-argcomplete@${PY_FLAVOR} \
		??/py-crcmod@${PY_FLAVOR} \
		??/py-graphviz@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-pycups@${PY_FLAVOR} \
		??/py-pyserial@${PY_FLAVOR} \
		??/py-pyxdg@${PY_FLAVOR} \
		??/py-rpyc@${PY_FLAVOR} \
		??/py-xtermcolor@${PY_FLAVOR} \
		??/py-z3-solver@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
