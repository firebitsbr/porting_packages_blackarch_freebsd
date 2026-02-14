PORTNAME=	quark-engine
DISTVERSION=	21.6.2
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	An Obfuscation-Neglect Android Malware Scoring System.
WWW=		https://github.com/quark-engine/quark-engine

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/androguard \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-gitpython@${PY_FLAVOR} \
		??/py-graphviz@${PY_FLAVOR} \
		??/py-prettytable@${PY_FLAVOR} \
		??/py-tqdm@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
