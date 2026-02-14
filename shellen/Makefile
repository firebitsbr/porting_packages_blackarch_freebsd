PORTNAME=	shellen
DISTVERSION=	66.c0c5f83
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Interactive shellcoding environment to easily craft shellcodes.
WWW=		https://github.com/merrychap/shellen

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/py-capstone@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-keystone@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		??/py-termcolor@${PY_FLAVOR} \
		??/py-terminaltables@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
