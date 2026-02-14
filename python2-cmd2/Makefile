PORTNAME=	python2-cmd2
DISTVERSION=	0.8.9
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A tool for building interactive command line applications in Python.
WWW=		https://pypi.org/project/cmd2/#files

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-enum34@${PY_FLAVOR} \
		??/py-pyparsing@${PY_FLAVOR} \
		??/py-pyperclip@${PY_FLAVOR} \
		??/py-subprocess32@${PY_FLAVOR} \
		??/py-wcwidth@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python3


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
