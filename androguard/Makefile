PORTNAME=	androguard
DISTVERSION=	3.3.5
CATEGORIES=	freebsd security

MAINTAINER=	mauro.risonho@gmail.com
COMMENT=	Reverse engineering, Malware and goodware analysis of Android applications and more.
WWW=		https://github.com/androguard/androguard

LICENSE=	GPLv3 # Defaulting to GPLv3

BUILD_DEPENDS=	devel/git \
		devel/py-setuptools@${PY_FLAVOR}

RUN_DEPENDS=	??/ipython \
		??/py-asn1crypto@${PY_FLAVOR} \
		??/py-click@${PY_FLAVOR} \
		??/py-colorama@${PY_FLAVOR} \
		??/py-future@${PY_FLAVOR} \
		??/py-lxml@${PY_FLAVOR} \
		??/py-matplotlib@${PY_FLAVOR} \
		??/py-networkx@${PY_FLAVOR} \
		??/py-pydot@${PY_FLAVOR} \
		??/py-pygments@${PY_FLAVOR} \
		lang/python


USE_GITHUB=	yes
GH_ACCOUNT=	# Needs manual check

.include <bsd.port.mk>
