PORTNAME=	ipython2
DISTVERSION=	5.10.0
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Provides a rich toolkit to help you make the most out of using Python interactively.
WWW=		https://pypi.org/project/ipython/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-backports.shutil_get_terminal_size@${PY_FLAVOR} \
		??/py-pathlib@${PY_FLAVOR} \
		??/py-pexpect@${PY_FLAVOR} \
		??/py-pickleshare@${PY_FLAVOR} \
		??/py-prompt_toolkit1@${PY_FLAVOR} \
		??/py-simplegeneric@${PY_FLAVOR} \
		??/py-traitlets@${PY_FLAVOR} \
		??/sqlite \
		devel/py-setuptools@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
