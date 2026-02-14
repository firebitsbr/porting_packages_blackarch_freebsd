PORTNAME=	pwncat-caleb
DISTVERSION=	v0.5.4.r11.g37f04d4
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	A post-exploitation platform.
WWW=		https://github.com/calebstewart/pwncat

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	??/py-build@${PY_FLAVOR} \
		??/py-wheel@${PY_FLAVOR} \
		devel/git \
		devel/py-pip@${PY_FLAVOR}

RUN_DEPENDS=	??/py-jinja@${PY_FLAVOR} \
		??/py-netifaces@${PY_FLAVOR} \
		??/py-packaging@${PY_FLAVOR} \
		??/py-paramiko@${PY_FLAVOR} \
		??/py-prompt_toolkit@${PY_FLAVOR} \
		??/py-pycryptodome@${PY_FLAVOR} \
		??/py-rapidjson@${PY_FLAVOR} \
		??/py-rich@${PY_FLAVOR} \
		??/py-zodb@${PY_FLAVOR} \
		??/py-zodburi@${PY_FLAVOR} \
		lang/python \
		www/py-requests@${PY_FLAVOR}


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
