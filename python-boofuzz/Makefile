PORTNAME=	python-boofuzz
DISTVERSION=	0.4.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Boofuzz is a fork of Sulley fuzzing framework and aims for extensibility. The goal: fuzz everything.
WWW=		https://pypi.org/project/boofuzz/

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/impacket \
		??/py-attrs@${PY_FLAVOR} \
		??/py-backports.shutil-get-terminal-size@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-flask@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-psutil@${PY_FLAVOR} \
		??/py-pydot@${PY_FLAVOR} \
		??/py-pyserial@${PY_FLAVOR} \
		??/py-tornado@${PY_FLAVOR} \
		devel/py-six@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
