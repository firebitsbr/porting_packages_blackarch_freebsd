PORTNAME=	featherduster
DISTVERSION=	191.9229158
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An automated, modular cryptanalysis tool.
WWW=		https://github.com/nccgroup/featherduster

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/ncurses \
		??/py-gmpy@${PY_FLAVOR} \
		??/py-ishell@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-singlefile@${PY_FLAVOR} \
		??/readline \
		lang/python3 \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
